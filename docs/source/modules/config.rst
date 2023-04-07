.. _modules_config:

.. include:: ../_include/head.rst

======
Status
======

**STATE**: testing

**TESTS**: `Playbook <https://github.com/ansibleguy/collection_linuxha/blob/latest/tests/config.yml>`_


Definition
**********

.. include:: ../_include/param_basic.rst

Info
****

Module to pull the current LinuxHA configuration.

Examples
********

.. code-block:: yaml

    - hosts: node1
      gather_facts: false
      become: true
      tasks:
        - name: Example
          ansibleguy.linuxha.config:

        - name: Pulling current config
          ansibleguy.linuxha.config:
          register: lha_config

        - name: Showing status
          ansible.builtin.debug:
            var: lha_config.data
