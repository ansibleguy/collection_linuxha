#!/usr/bin/env python3

# Copyright: (C) 2023, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.linuxha.plugins.module_utils.defaults import LHA_MOD_ARGS_MAIN
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.crmsh import crmsh_exec
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.parse.status import status_full
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.parse.util import extract_debug

DOCUMENTATION = 'https://linuxha.ansibleguy.net/en/latest/modules/status.html'
EXAMPLES = 'https://linuxha.ansibleguy.net/en/latest/modules/status.html'


def run_module():
    module_args = dict(
        **LHA_MOD_ARGS_MAIN,
        detailed=dict(
            type='bool', required=False, default=False, aliases=['detail'],
            description='Return a more detailed status parsed from XML output',
        ),
        subset=dict(
            type='list', elements='str', required=False, aliases=['parse', 'sub'],
            default=['cluster', 'nodes', 'operations', 'resources'],
            description="Provide subsets to parse (ignored if 'detailed: true' is set)",
        ),
        time_format=dict(
            type='str', required=False, default='%Y-%m-%d %H:%M:%S', aliases=['t_fmt'],
            description="Datetime format to use for translating timestamps (ignored if 'detailed: true' is set)",
        ),
    )

    result = dict(
        changed=False,
        rc=0,
        stdout='',
        stderr='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    if module.params['detailed']:
        _, raw_status = crmsh_exec(
            m=module,
            r=result,
            cmd=['status', 'xml'],
            check_safe=True, output=True,
        )
        raw_status = extract_debug(p=module.params, r=result, raw=raw_status)
        result['_data'] = raw_status

    else:
        result['data'] = status_full(m=module, r=result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
