#!/usr/bin/env python3

# Copyright: (C) 2023, AnsibleGuy <guy@ansibleguy.net>
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.linuxha.plugins.module_utils.defaults import LHA_MOD_ARGS
from ansible_collections.ansibleguy.linuxha.plugins.module_utils.crmsh import crmsh_exec

DOCUMENTATION = 'https://linuxha.ansibleguy.net/en/latest/modules/raw.html'
EXAMPLES = 'https://linuxha.ansibleguy.net/en/latest/modules/raw.html'


def run_module():
    module_args = dict(
        **LHA_MOD_ARGS,
        cmd=dict(
            type='list', elements='str', required=True, aliases=['c', 'command'],
            description='Raw command to pass to crm-shell',
        ),
        fail=dict(
            type='bool', required=False, default=True, aliases=['f'],
            description='Fail module if command fails',
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

    cmd = module.params['cmd']
    if len(cmd) == 1 and cmd[0].find(' ') != -1:
        cmd = cmd[0].split(' ')

    crmsh_exec(m=module, r=result, cmd=cmd)

    if not module.check_mode:
        result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
