from ansible.module_utils.basic import AnsibleModule


def exit_bug(m: AnsibleModule, msg: str):
    m.fail_json(f"THIS MIGHT BE A MODULE-BUG: {msg}")


def exit_debug(m: AnsibleModule, msg: str):
    m.fail_json(f"DEBUG INFO: {msg}")


def exit_env(m: AnsibleModule, msg: str):
    m.fail_json(f"ENVIRONMENTAL ERROR: {msg}")


def exit_cnf(m: AnsibleModule, msg: str):
    m.fail_json(f"CONFIG ERROR: {msg}")
