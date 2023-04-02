.. _usage_basic:

.. include:: ../_include/head.rst

=========
3 - Basic
=========

Run once
********

Cluster-specific operations **must only be executed on ONE NODE AT A TIME**!

Such operations include:

* Resource actions
* most Node actions
* Configuration changes

You can achieve this easily by either:

* use the 'run_once: true' parameter (*dynamic*)

  .. code-block:: yaml

      - hosts: linuxha
        gather_facts: false
        become: true
        tasks:
          - name: Run once per cluster
            ansibleguy.linuxha.raw:
              cmd: 'to execute'
            run_once: true

* add an inventory-group of 'leader-nodes' that will be used as execution targets (*static but working for multi-cluster setup*)

  inventory

  .. code-block:: yaml

      ---

      all:
        hosts:
          # cluster 1
          node1:
          node2:
          # cluster 2
          node3:
          node4:
        children:
          linuxha:
            hosts:
              node1:
              node2:
              node3:
              node4:
          linuxha_leader:
            hosts:
              node1:
              node3:


  playbook

  .. code-block:: yaml

      - hosts: linuxha_leader
        gather_facts: false
        become: true
        tasks:
          - name: Run once per cluster
            ansibleguy.linuxha.raw:
              cmd: 'to execute'
