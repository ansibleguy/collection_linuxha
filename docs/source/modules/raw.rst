.. _modules_raw:

.. include:: ../_include/head.rst

===
Raw
===

**STATE**: unstable

**TESTS**: `Playbook <https://github.com/ansibleguy/collection_linuxha/blob/latest/tests/raw.yml>`_

**Docs**: `crm-shell <https://crmsh.github.io/man-2.0/>`_


Definition
**********

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Aliases", "Comment"
    :widths: 15 10 10 10 10 45

    "cmd","string","true","\-","command, c", "Raw command to pass to crm-shell"
    "fail","boolean","false","true","f", "Fail module if command fails"

.. include:: ../_include/param_basic.rst

Info
****

Will pass any command to 'crm-shell'.


.. warning::

    THERE IS NO CLIENT-SIDE CONFIG VALIDATION!


Examples
********

.. code-block:: yaml

    - hosts: node1
      gather_facts: false
      become: true
      tasks:
        - name: Example
          ansibleguy.linuxha.raw:
            cmd: 'to execute'
            # fail: true  # Fail module if command fails
            # force: false
            # wait: false
            # debug: false

        - name: Pulling raw running-config
          ansibleguy.linuxha.raw:
            cmd: 'configure show'
          register: lha_cnf

        - name: Showing config
          ansible.builtin.debug:
            var: lha_cnf.stdout_lines

        - name: Disabling stonith
          ansibleguy.linuxha.raw:
            cmd: 'configure property stonith-enabled=false'

        - name: Adding resource
          ansibleguy.linuxha.raw:
            cmd: 'configure primitive vip1 IPaddr2 params ip=10.15.12.1 nic=eno1'

        - name: Pulling raw status
          ansibleguy.linuxha.raw:
            cmd: 'status bynode'
          register: lha_status

        - name: Showing status
          ansible.builtin.debug:
            var: lha_status.stdout_lines
