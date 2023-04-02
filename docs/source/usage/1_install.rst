.. _usage_install:

.. include:: ../_include/head.rst

================
1 - Installation
================


Ansible
*******

See `the documentation <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#pip-install>`_ on how to install Ansible.

Dependencies
************

Install
=======

You will have to install the LinuxHA packages on the target server:

* `LinuxHA <https://wiki.clusterlabs.org/wiki/Install>`_ (packages: `corosync <https://github.com/corosync/corosync>`_ and `pacemaker <https://github.com/ClusterLabs/pacemaker>`_)
* `crm shell <https://github.com/ClusterLabs/crmsh>`_ (package: crmsh)

.. code-block:: bash

    sudo apt install corosync pacemaker crmsh



The `xmltodict python module <https://github.com/martinblech/xmltodict>`_ is used to parse config!

It is only needed on the Ansible controller!

.. code-block:: bash

    python3 -m pip install xmltodict

Configure
=========

After that - configure the basic cluster using the 'corosync.conf' file.

See: :ref:`Docs <usage_config>`


Collection
**********

.. code-block:: bash

    # stable version:
    ansible-galaxy collection install ansibleguy.linuxha

    # latest version:
    ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git

    # install to specific directory for easier development
    cd $PLAYBOOK_DIR
    ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git -p ./collections
