.. _modules_config:

.. include:: ../_include/head.rst

======
Status
======

**STATE**: unstable

**TESTS**: `Playbook <https://github.com/ansibleguy/collection_linuxha/blob/latest/tests/config.yml>`_


Definition
**********

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Aliases", "Comment"
    :widths: 15 10 10 10 10 45

    "raw","boolean","false","false","\-", "Return the full un-modified/-simplified config-dump"
    "subset","list","false","['groups', 'locations', 'nodes', 'orders', 'primitives', 'properties', 'clones']","parse, sub", "Provide one or multiple status-subsets to parse (*ignored if 'raw: true' is set*)"


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
            # raw: false
            # subset: ['groups', 'locations', 'nodes', 'orders', 'primitives', 'properties', 'clones']

        - name: Pulling current config
          ansibleguy.linuxha.config:
          register: lha_config

        - name: Showing config
          ansible.builtin.debug:
            var: lha_config.data

        # {
        #     "clones": {
        #         "ANSIBLE_TEST_3_5": [
        #             "ANSIBLE_TEST_3_4"
        #         ]
        #     },
        #     "groups": {
        #         "ANSIBLE_TEST_3_6": [
        #             "ANSIBLE_TEST_3_1",
        #             "ANSIBLE_TEST_3_2"
        #         ]
        #     },
        #     "locations": {
        #         "ANSIBLE_TEST_3_8": {
        #             "node": "node2",
        #             "role": "Started",
        #             "rsc": "ANSIBLE_TEST_3_3",
        #             "score": "INFINITY"
        #         }
        #     },
        #     "nodes": {
        #         "node1": 1,
        #         "node2": 2
        #     },
        #     "orders": {
        #         "ANSIBLE_TEST_3_7": {
        #             "first": "ANSIBLE_TEST_3_3",
        #             "first-action": "start",
        #             "kind": "Mandatory",
        #             "then": "ANSIBLE_TEST_3_1",
        #             "then-action": "start"
        #         }
        #     },
        #     "primitives": {
        #         "ANSIBLE_TEST_3_1": {
        #             "class": "ocf",
        #             "params": {
        #                 "ip": "127.100.1.2",
        #                 "nic": "lo"
        #             },
        #             "provider": "heartbeat",
        #             "type": "IPaddr2"
        #         },
        #         "ANSIBLE_TEST_3_2": {
        #             "class": "ocf",
        #             "params": {
        #                 "ip": "127.100.1.3",
        #                 "nic": "lo"
        #             },
        #             "provider": "heartbeat",
        #             "type": "IPaddr2"
        #         },
        #         "ANSIBLE_TEST_3_3": {
        #             "class": "ocf",
        #             "params": {
        #                 "ip": "127.100.1.4",
        #                 "nic": "lo"
        #             },
        #             "provider": "heartbeat",
        #             "type": "IPaddr2"
        #         }
        #     },
        #     "properties": {
        #         "cluster-infrastructure": "corosync",
        #         "cluster-name": "debian",
        #         "dc-version": "2.0.5-ba59be7122",
        #         "have-watchdog": false,
        #         "last-lrm-refresh": 1680443090,
        #         "stonith-enabled": false
        #     }
        # }

        - name: Pulling only a subset of the current config
          ansibleguy.linuxha.config:
            subset: ['properties', 'primitives']
          register: lha_config_subset

        - name: Showing config subset
          ansible.builtin.debug:
            var: lha_config_subset.data

        # {
        #     "primitives": {
        #         "ANSIBLE_TEST_3_1": {
        #             "class": "ocf",
        #             "params": {
        #                 "ip": "127.100.1.2",
        #                 "nic": "lo"
        #             },
        #             "provider": "heartbeat",
        #             "type": "IPaddr2"
        #         },
        #         "ANSIBLE_TEST_3_2": {
        #             "class": "ocf",
        #             "params": {
        #                 "ip": "127.100.1.3",
        #                 "nic": "lo"
        #             },
        #             "provider": "heartbeat",
        #             "type": "IPaddr2"
        #         },
        #         "ANSIBLE_TEST_3_3": {
        #             "class": "ocf",
        #             "params": {
        #                 "ip": "127.100.1.4",
        #                 "nic": "lo"
        #             },
        #             "provider": "heartbeat",
        #             "type": "IPaddr2"
        #         }
        #     },
        #     "properties": {
        #         "cluster-infrastructure": "corosync",
        #         "cluster-name": "debian",
        #         "dc-version": "2.0.5-ba59be7122",
        #         "have-watchdog": false,
        #         "last-lrm-refresh": 1680443090,
        #         "stonith-enabled": false
        #     }
        # }

        - name: Pulling current config in raw-format
          ansibleguy.linuxha.config:
            raw: true
          register: lha_raw_config

        - name: Showing raw-config
          ansible.builtin.debug:
            var: lha_raw_config.data

        # {
        #     "admin_epoch": "0",
        #     "cib-last-written": "Sat Apr  8 16:33:40 2023",
        #     "configuration": {
        #         "constraints": {
        #             "rsc_location": {
        #                 "id": "ANSIBLE_TEST_3_8",
        #                 "node": "node2",
        #                 "role": "Started",
        #                 "rsc": "ANSIBLE_TEST_3_3",
        #                 "score": "INFINITY"
        #             },
        #             "rsc_order": {
        #                 "first": "ANSIBLE_TEST_3_3",
        #                 "first-action": "start",
        #                 "id": "ANSIBLE_TEST_3_7",
        #                 "kind": "Mandatory",
        #                 "then": "ANSIBLE_TEST_3_1",
        #                 "then-action": "start"
        #             }
        #         },
        #         "crm_config": {
        #             "cluster_property_set": {
        #                 "id": "cib-bootstrap-options",
        #                 "nvpair": [
        #                     {
        #                         "id": "cib-bootstrap-options-have-watchdog",
        #                         "name": "have-watchdog",
        #                         "value": "false"
        #                     },
        #                     {
        #                         "id": "cib-bootstrap-options-dc-version",
        #                         "name": "dc-version",
        #                         "value": "2.0.5-ba59be7122"
        #                     },
        #                     {
        #                         "id": "cib-bootstrap-options-cluster-infrastructure",
        #                         "name": "cluster-infrastructure",
        #                         "value": "corosync"
        #                     },
        #                     {
        #                         "id": "cib-bootstrap-options-cluster-name",
        #                         "name": "cluster-name",
        #                         "value": "debian"
        #                     },
        #                     {
        #                         "id": "cib-bootstrap-options-stonith-enabled",
        #                         "name": "stonith-enabled",
        #                         "value": "false"
        #                     },
        #                     {
        #                         "id": "cib-bootstrap-options-last-lrm-refresh",
        #                         "name": "last-lrm-refresh",
        #                         "value": "1680443090"
        #                     }
        #                 ]
        #             }
        #         },
        #         "nodes": {
        #             "node": [
        #                 {
        #                     "id": "1",
        #                     "uname": "node1"
        #                 },
        #                 {
        #                     "id": "2",
        #                     "uname": "node2"
        #                 }
        #             ]
        #         },
        #         "resources": {
        #             "clone": {
        #                 "id": "ANSIBLE_TEST_3_5",
        #                 "primitive": {
        #                     "class": "ocf",
        #                     "id": "ANSIBLE_TEST_3_4",
        #                     "instance_attributes": {
        #                         "id": "ANSIBLE_TEST_3_4-instance_attributes",
        #                         "nvpair": {
        #                             "id": "ANSIBLE_TEST_3_4-instance_attributes-host_list",
        #                             "name": "host_list",
        #                             "value": "1.1.1.1 8.8.8.8"
        #                         }
        #                     },
        #                     "operations": {
        #                         "op": {
        #                             "id": "ANSIBLE_TEST_3_4-monitor-5s",
        #                             "interval": "5s",
        #                             "name": "monitor",
        #                             "on-fail": "restart",
        #                             "timeout": "60"
        #                         }
        #                     },
        #                     "provider": "pacemaker",
        #                     "type": "ping"
        #                 }
        #             },
        #             "group": {
        #                 "id": "ANSIBLE_TEST_3_6",
        #                 "primitive": [
        #                     {
        #                         "class": "ocf",
        #                         "id": "ANSIBLE_TEST_3_1",
        #                         "instance_attributes": {
        #                             "id": "ANSIBLE_TEST_3_1-instance_attributes",
        #                             "nvpair": [
        #                                 {
        #                                     "id": "ANSIBLE_TEST_3_1-instance_attributes-ip",
        #                                     "name": "ip",
        #                                     "value": "127.100.1.2"
        #                                 },
        #                                 {
        #                                     "id": "ANSIBLE_TEST_3_1-instance_attributes-nic",
        #                                     "name": "nic",
        #                                     "value": "lo"
        #                                 }
        #                             ]
        #                         },
        #                         "provider": "heartbeat",
        #                         "type": "IPaddr2"
        #                     },
        #                     {
        #                         "class": "ocf",
        #                         "id": "ANSIBLE_TEST_3_2",
        #                         "instance_attributes": {
        #                             "id": "ANSIBLE_TEST_3_2-instance_attributes",
        #                             "nvpair": [
        #                                 {
        #                                     "id": "ANSIBLE_TEST_3_2-instance_attributes-ip",
        #                                     "name": "ip",
        #                                     "value": "127.100.1.3"
        #                                 },
        #                                 {
        #                                     "id": "ANSIBLE_TEST_3_2-instance_attributes-nic",
        #                                     "name": "nic",
        #                                     "value": "lo"
        #                                 }
        #                             ]
        #                         },
        #                         "provider": "heartbeat",
        #                         "type": "IPaddr2"
        #                     }
        #                 ]
        #             },
        #             "primitive": {
        #                 "class": "ocf",
        #                 "id": "ANSIBLE_TEST_3_3",
        #                 "instance_attributes": {
        #                     "id": "ANSIBLE_TEST_3_3-instance_attributes",
        #                     "nvpair": [
        #                         {
        #                             "id": "ANSIBLE_TEST_3_3-instance_attributes-ip",
        #                             "name": "ip",
        #                             "value": "127.100.1.4"
        #                         },
        #                         {
        #                             "id": "ANSIBLE_TEST_3_3-instance_attributes-nic",
        #                             "name": "nic",
        #                             "value": "lo"
        #                         }
        #                     ]
        #                 },
        #                 "provider": "heartbeat",
        #                 "type": "IPaddr2"
        #             }
        #         }
        #     },
        #     "crm_feature_set": "3.6.1",
        #     "dc-uuid": "1",
        #     "epoch": "418",
        #     "have-quorum": "1",
        #     "num_updates": "12",
        #     "update-client": "cibadmin",
        #     "update-origin": "node1",
        #     "update-user": "root",
        #     "validate-with": "pacemaker-3.5"
        # }
