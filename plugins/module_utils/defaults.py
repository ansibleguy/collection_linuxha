LHA_MOD_ARGS_MAIN = dict(
    debug=dict(type='bool', required=False, default=False),
)

LHA_MOD_ARGS = dict(
    wait=dict(
        type='bool', required=False, default=False,
        description='Make crm wait for the cluster transition to finish (for the changes to take effect) '
                    'after each processed line'
    ),
    force=dict(
        type='bool', required=False, default=False,
        description='Make crm proceed with applying changes where it would normally ask the user to confirm before '
                    'proceeding. This option is mainly useful in scripts, and should be used with care'
    ),
    debug=LHA_MOD_ARGS_MAIN['debug'],
)
