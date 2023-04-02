from datetime import datetime

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.linuxha.plugins.module_utils.handler import debug
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.crmsh import crmsh_exec
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.parse.util import \
    cut_block, extract_post, extract

DATETIME_FORMAT = '%a %b %d %H:%M:%S %Y'
# 'Sun Apr  2 15:46:05 2023'


def cluster(m: AnsibleModule, raw_status: str) -> dict:
    debug(m=m, msg='Status - parsing cluster!')
    raw = cut_block(raw=raw_status, start='Cluster Summary:')
    return dict(
        dc=extract(raw=raw, pre='Current DC: ', post=' '),
        version=extract(raw=raw, pre='Current DC: ', post=')', mid=' ', mid_rsplit=True, mid_idx=1),
        updated=datetime.strptime(
            extract(raw=raw, pre='Last updated: ', post='\n'), DATETIME_FORMAT
        ).strftime(m.params['time_format']),
        changed_time=datetime.strptime(
            extract(raw=raw, pre='Last change: ', post=' by root'), DATETIME_FORMAT
        ).strftime(m.params['time_format']),
        changed_node=extract(raw=raw, pre='Last change: ', post='\n', mid='on ', mid_rsplit=True, mid_idx=1),
        changed_user=extract(raw=raw, pre='Last change: ', post=' via', mid='by ', mid_rsplit=True, mid_idx=1),
        changed_via=extract(raw=raw, pre='Last change: ', post=' on', mid='via ', mid_rsplit=True, mid_idx=1),
        node_count=int(extract_post(raw=raw, post=' nodes configured', pre='* ')),
        resource_count=int(extract_post(raw=raw, post=' resource instance', pre='* ')),
    )


def _parse_node_resources(m: AnsibleModule, raw_node: str) -> dict:
    _resources = {}

    if raw_node.find('Resources:\n') == -1:
        return _resources

    for raw_res in raw_node.split('Resources:\n')[1].split('\n'):
        try:
            _res_name = raw_res.split('* ', 1)[1].split('\t', 1)[0]
            _res_type = raw_res.split('\t', 2)[1].strip().replace('(', '').split(')', 1)[0]
            _res_type_class = _res_type.split('::', 1)[0] if _res_type.find('::') != -1 else None
            _res_type_provider = _res_type.rsplit(':', 1)[0]
            if _res_type_provider.find(':') != -1:
                _res_type_provider = _res_type_provider.rsplit(':', 1)[1]

            _resources[_res_name] = dict(
                state=raw_res.split('\t', 2)[2].strip(),
                resource={
                    'class': _res_type_class,
                    'provider': _res_type_provider,
                    'type': _res_type.rsplit(':', 1)[1],
                }
            )

        except IndexError:
            debug(m=m, msg=f"Syntax error on parsing raw status-node: '{raw_node}'")
            continue

    return _resources


def nodes(m: AnsibleModule, raw_status: str) -> dict:
    # {node: {status, resources: {state, resource: {class: 'cls', provider: 'pvd', type: 'type'}}}}

    debug(m=m, msg='Status - parsing nodes!')
    raw = cut_block(raw=raw_status, start='\nNode List:')
    data = {}

    for idx, node in enumerate(raw.split('* Node')):
        if idx == 0:
            continue

        _name = node.split(':', 1)[0].strip()
        _status = node.split(':', 2)[1].strip()

        data[_name] = dict(
            status=_status,
            resources=_parse_node_resources(m=m, raw_node=node),
        )

    return data


def resources(m: AnsibleModule, raw_status: str) -> dict:
    # {resource: {nodes: {node: state, node: state}, resource: {class: 'cls', provider: 'pvd', type: 'type'}}}
    debug(m=m, msg='Status - parsing resources!')
    data = {}

    for _node_name, _node_values in nodes(m=m, raw_status=raw_status).items():
        for _res_name, _res_values in _node_values['resources'].items():
            if _res_name not in data:
                data[_res_name] = {'nodes': {}, 'resource': _res_values['resource']}

            data[_res_name]['nodes'][_node_name] = _res_values['state']

    # todo: interactive resources
    # raw_irs = cut_block(raw=raw_status, start='\nInactive Resources:')
    # Inactive Resources:
    #   * No inactive resources

    return data


def operations(m: AnsibleModule, raw_status: str) -> dict:
    raw = cut_block(raw=raw_status, start='\nOperations:')
    debug(m=m, msg='Status - parsing operations!')
    data = {}

    for idx, node in enumerate(raw.split('* Node:')):
        if idx == 0:
            continue

        _node_name = node.split(':', 1)[0].strip()
        _ops = {}

        for op_idx, op in enumerate(node.split('\n    * ')):
            if op_idx == 0:
                continue

            _res_name = op.split(':', 1)[0]

            if _res_name not in _ops:
                _ops[_res_name] = {}

            _op_time = datetime.strptime(
                extract(raw=op, pre='last-run="', post='"'), DATETIME_FORMAT
            ).strftime(m.params['time_format'])

            _ops[_res_name][_op_time] = dict(
                migration_threshold=extract(raw=op, pre='migration-threshold=', post=':'),
                operation_id=extract(raw=op, pre='* (', post=')'),
                operation=extract(raw=op, pre='* (', post=':', mid=' ', mid_idx=1),
                change=datetime.strptime(
                    extract(raw=op, pre='last-rc-change="', post='"'), DATETIME_FORMAT
                ).strftime(m.params['time_format']),
                time_exec=extract(raw=op, pre='exec-time="', post='"'),
                time_queue=extract(raw=op, pre='queue-time="', post='"'),
                rc=extract(raw=op, pre='rc=', post=' '),
                status=extract(raw=op, pre='rc=', post=')', mid='(', mid_idx=1),
            )

        data[_node_name] = _ops

    return data


def status_full(m: AnsibleModule, r: dict, raw_status: str = None) -> dict:
    if raw_status is None:
        _, raw_status = crmsh_exec(
            m=m, r=r,
            cmd=['status', 'full', '|', 'cat'],
            check_safe=True, output=True,
        )

    data = {}

    for s, f in {
        'cluster': cluster,
        'nodes': nodes,
        'resources': resources,
        'operations': operations,
    }.items():
        if s in m.params['subset']:
            data[s] = f(m=m, raw_status=raw_status)

    return data
