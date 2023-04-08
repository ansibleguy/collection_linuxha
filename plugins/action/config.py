from xml.parsers.expat import ExpatError

from xmltodict import parse as parse_xml

from ansible.plugins.action import ActionBase


def ensure_list(data: (list, dict, str)) -> list:
    if not isinstance(data, list):
        return [data]

    return data


def type_correction(data: dict) -> dict:
    for k, v in data.items():
        if not isinstance(v, str):
            data[k] = v

        elif v.isnumeric():
            data[k] = int(v)

        elif v == 'true':
            data[k] = True

        elif v == 'false':
            data[k] = False

    return data


def build_params(nvpairs: (list, dict)) -> dict:
    params = {}

    for nv in ensure_list(nvpairs):
        params[nv['name']] = nv['value']

    return type_correction(params)


def parse_properties(raw_props: dict) -> dict:
    key1, key2 = 'cluster_property_set', 'nvpair'
    props = {}

    if key1 in raw_props and key2 in raw_props[key1]:
        props = build_params(raw_props[key1][key2])

    return type_correction(props)


def parse_nodes(raw_nodes: dict) -> dict:
    key1 = 'node'
    nodes = {}

    if key1 in raw_nodes:
        for node in ensure_list(raw_nodes[key1]):
            nodes[node['uname']] = int(node['id'])

    return nodes


def parse_primitives(raw_prims: (dict, list)) -> dict:
    key1, key2 = 'instance_attributes', 'nvpair'
    prims = {}

    for prim in ensure_list(raw_prims):
        params = {}
        if key1 in prim and key2 in prim[key1]:
            params = build_params(prim[key1][key2])

        prims[prim['id']] = {
            'class': prim['class'] if 'class' in prim else None,
            'provider': prim['provider'] if 'provider' in prim else None,
            'type': prim['type'] if 'type' in prim else None,
            'params': params,
        }

    return prims


def parse_groups_clones(raw_items: (dict, list)) -> dict:
    items = {}

    for item in ensure_list(raw_items):
        items[item['id']] = [entry['id'] for entry in ensure_list(item['primitive'])]

    return items


def parse_constraints(raw_cnsts: (None, dict)) -> (dict, None):
    processed = ['rsc_location', 'rsc_order']
    cnsts = {}

    if raw_cnsts is None:
        return None

    for k, v in raw_cnsts.items():
        if k in processed:
            continue

        # pass output 1-to-1 if no special parsing is defined
        cnsts[k] = v

    if len(cnsts) == 0:
        return None

    return cnsts


def parse_locations_orders(raw_items: (dict, list)) -> dict:
    parsed = {}

    for item in ensure_list(raw_items):
        item_id = item['id']
        item.pop('id')
        parsed[item_id] = item

    return parsed


PARSE_MAP = {
    'crm_config': {'out_key': 'properties', 'func': parse_properties},
    'nodes': {'out_key': 'nodes', 'func': parse_nodes},
    'resources': {
        'sub_keys': {
            'primitive': {'out_key': 'primitives', 'func': parse_primitives},
            'group': {'out_key': 'groups', 'func': parse_groups_clones},
            'clone': {'out_key': 'clones', 'func': parse_groups_clones},
        },
    },
    'constraints': {
        'sub_keys': {
            'rsc_location': {'out_key': 'locations', 'func': parse_locations_orders},
            'rsc_order': {'out_key': 'orders', 'func': parse_locations_orders},
        },
    }
}


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)
        module_output = self._execute_module(
            module_name='ansibleguy.linuxha.config',
            module_args=self._task.args,
            task_vars=task_vars,
            tmp=tmp
        )
        params = module_output['_params']
        result = module_output.copy()
        result.pop('_data')
        result.pop('_params')

        try:
            raw_data = parse_xml(
                module_output['_data'],
                attr_prefix=''
            )['cib']

        except ExpatError as e:
            result['rc'] = 1
            result['error'] = str(e)
            return result

        if params['raw']:
            result['data'] = raw_data
            return result

        self._debug(params=params, result=result, raw_data=raw_data)
        return self._parse(params=params, result=result, raw_data=raw_data)

    @staticmethod
    def _debug(params: dict, result: dict, raw_data: dict):
        if params['debug']:
            result['raw'] = raw_data

            if 'debug' not in result:
                result['debug'] = []

            result['debug'].append(
                {k: v for k, v in raw_data.items() if k != 'configuration'}
            )

    def _parse(self, params: dict, result: dict, raw_data: dict) -> dict:
        raw_config = raw_data['configuration']
        result['data'] = {}

        for key in raw_config:
            if raw_config[key] is None:
                continue

            if key in PARSE_MAP:
                if 'sub_keys' in PARSE_MAP[key]:
                    for sub_key in raw_config[key]:
                        if sub_key in PARSE_MAP[key]['sub_keys']:
                            map_cnf = PARSE_MAP[key]['sub_keys'][sub_key]

                            if params['subset'] is not None:
                                if map_cnf['out_key'] not in params['subset']:
                                    continue

                            result['data'][map_cnf['out_key']] = map_cnf['func'](
                                raw_config[key][sub_key]
                            )

                        else:
                            # pass output 1-to-1 if no special parsing is defined
                            result['data'][f"{key}_{sub_key}"] = raw_config[key][sub_key]

                else:
                    map_cnf = PARSE_MAP[key]

                    if params['subset'] is not None:
                        if map_cnf['out_key'] not in params['subset']:
                            continue

                    result['data'][map_cnf['out_key']] = map_cnf['func'](
                        raw_config[key]
                    )

            else:
                # pass output 1-to-1 if no special parsing is defined
                result['data'][key] = raw_config[key]

        self._parse_special_cases(params=params, raw_config=raw_config, result=result)
        return result

    @staticmethod
    def _parse_special_cases(params: dict, raw_config: dict, result: dict):
        # primitives in groups
        if params['subset'] is None or 'primitives' in params['subset']:
            if 'resources' in raw_config and raw_config['resources'] is not None:
                if 'group' in raw_config['resources']:
                    prims = result['data']['primitives'] if 'primitives' in result['data'] else {}

                    for grp in ensure_list(raw_config['resources']['group']):
                        if 'primitive' in grp:
                            for prim in ensure_list(grp['primitive']):
                                if prim['id'] not in prims:
                                    prims = {**parse_primitives(prim), **prims}

                    result['data']['primitives'] = prims
