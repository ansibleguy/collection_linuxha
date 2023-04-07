#!/usr/bin/env python3

# Copyright: (C) 2023, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.linuxha.plugins.module_utils.defaults import LHA_MOD_ARGS_MAIN
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.crmsh import crmsh_exec
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.parse.util import extract_debug

DOCUMENTATION = 'https://linuxha.ansibleguy.net/en/latest/modules/config.html'
EXAMPLES = 'https://linuxha.ansibleguy.net/en/latest/modules/config.html'


def run_module():
    module_args = LHA_MOD_ARGS_MAIN

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

    _, raw_config = crmsh_exec(
        m=module,
        r=result,
        cmd=['configure', 'show', 'xml'],
        check_safe=True, output=True,
    )
    raw_config = extract_debug(p=module.params, r=result, raw=raw_config)
    result['_action'] = raw_config

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
