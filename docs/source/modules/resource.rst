.. _modules_resource:

.. include:: ../_include/head.rst

========
Resource
========

**STATE**: development

**TESTS**: `Playbook <https://github.com/ansibleguy/collection_linuxha/blob/latest/tests/resource.yml>`_

**Docs**: `Resource <https://crmsh.github.io/man-2.0/>`_


Definition
**********

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Aliases", "Comment"
    :widths: 15 10 10 10 10 45

    "reload","boolean","false","true","\-", .. include:: ../_include/param_reload.rst

.. include:: ../_include/param_basic.rst

Info
****


Usage
*****


Examples
********

.. code-block:: yaml

    - hosts: localhost
      gather_facts: no
      tasks:
        - name: Example
          ansibleguy.linuxha.resource:
            # state: 'present'
            # enabled: true
            # debug: false

        - name: Adding

        - name: Removing

        - name: Listing hosts

        - name: Printing entries
