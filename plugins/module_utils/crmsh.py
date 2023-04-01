#!/usr/bin/env python3

from pathlib import Path
from os import geteuid

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ansibleguy.linuxha.plugins.module_utils.handler import exit_bug

DEFAULT_BIN = '/usr/sbin/crm'


def _run_cmd_wrapper(m: AnsibleModule, cmd: list, stdin: str = None) -> tuple:
    if m.params['debug']:
        m.warn(f"Executing command: '{cmd}'")

    return m.run_command(cmd, data=stdin)


def _build_cmd(m: AnsibleModule, args: list) -> list:
    if not isinstance(args, list):
        exit_bug(m=m, msg=f"Command arguments must be a list - got: {type(args)}!")

    cmd_bin = None

    if Path(DEFAULT_BIN).is_file():
        cmd_bin = DEFAULT_BIN

    if cmd_bin is None:
        rc, _, _ = _run_cmd_wrapper(m=m, cmd=['which', 'crm'])

        if rc == 0:
            cmd_bin = 'crm'

    if cmd_bin is None:
        m.fail_json(
            f"Executable 'crm' (crmsh) neither found in PATH nor at '{DEFAULT_BIN}'!"
        )

    cmd = [cmd_bin]
    cmd.extend(args)

    for param, check_args in {
        'debug': ['--debug', '-d'],
        'force': ['--force', '-F'],
        'wait': ['--wait', '-w'],
    }.items():
        if m.params[param] and all([arg not in cmd for arg in check_args]):
            cmd.append(check_args[0])

    return cmd


def _check_become(m: AnsibleModule) -> None:
    if geteuid() != 0:
        m.fail_json(
            "You need to set 'become: true' to execute crm-shell commands!"
        )


def _error_handling(m: AnsibleModule, r: dict, fail: bool, cmd: list) -> None:
    error = r['stderr']

    if r['stderr'].find('Could not connect to the CIB') != -1:
        error = 'CoroSync and/or Pacemaker seem to have problems communicating! ' \
                'Check the cluster is functioning correctly!'

        rc_sd, _, _ = _run_cmd_wrapper(m=m, cmd=['which', 'systemctl'])

        if rc_sd == 0:
            rc_cs, _, _ = _run_cmd_wrapper(m=m, cmd=['systemctl', 'is-active', 'corosync'])

            if rc_cs != 0:
                error = "Service 'corosync.service' not running!"

            else:
                rc_pm, _, _ = _run_cmd_wrapper(m=m, cmd=['systemctl', 'is-active', 'pacemaker'])

                if rc_pm != 0:
                    error = "Service 'pacemaker.service' not running!"

    msg = f"GOT ERROR RUNNING COMMAND '{' '.join(cmd)}'!"
    if fail:
        r['rc'], r['error'] = 1, msg

    else:
        m.warn(msg)


def _exec(m: AnsibleModule, r: dict, cmd: list, fail: bool, check_safe: bool) -> tuple:
    _check_become(m=m)
    cmd = _build_cmd(m=m, args=cmd)

    if not m.check_mode or check_safe:
        # NOTE: 'stdin=n' for possible yes/no prompt
        r['rc'], r['stdout'], r['stderr'] = _run_cmd_wrapper(m=m, cmd=cmd, stdin='n')

        if r['rc'] != 0:
            _error_handling(m=m, r=r, cmd=cmd, fail=fail)

    else:
        r['stdout'] = 'CHECK-MODE'

    return r['rc'] == 0, r['stdout']


def crmsh_exec(
        m: AnsibleModule, r: dict, cmd: list, output: bool = False,
        fail: bool = True, check_safe: bool = False,
) -> (bool, tuple):
    success, stdout = _exec(m=m, r=r, cmd=cmd, fail=fail, check_safe=check_safe)

    if output:
        return success, stdout

    return success
