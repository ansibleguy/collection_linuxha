.. _modules_basic:

.. include:: ../_include/head.rst

==========================
1 - Basic module arguments
==========================

**TESTS**: `Playbook <https://github.com/ansibleguy/collection_linuxha/blob/latest/tests/base.yml>`_

All modules
***********

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Comment"
    :widths: 15 10 10 10 55

    "debug","boolean","false","false","Enable debug output for module processing and crmsh"

Config/Action modules
*********************

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Comment"
    :widths: 15 10 10 10 55

    "wait","boolean","false","false","Make crm wait for the cluster transition to finish (for the changes to take effect) after each processed line"
    "force","boolean","false","false","Make crm proceed with applying changes where it would normally ask the user to confirm before proceeding. This option is mainly useful in scripts, and should be used with care"
