.. _modules_status:

.. include:: ../_include/head.rst

===
Raw
===

**STATE**: unstable

**TESTS**: `Playbook <https://github.com/ansibleguy/collection_linuxha/blob/latest/tests/status.yml>`_


Definition
**********

..  csv-table:: Definition
    :header: "Parameter", "Type", "Required", "Default", "Aliases", "Comment"
    :widths: 15 10 10 10 10 45

    "detailed","boolean","false","false","detail", "Return a more detailed status parsed from XML output"
    "subset","list","false","['cluster', 'nodes', 'resources', 'operations']","parse, sub", "Provide one or multiple status-subsets to parse (ignored if 'detailed: true' is set)"
    "time_format","string","false",%Y-%m-%d %H:%M:%S',"t_fmt", "Modify the datetime format used to parse timestamps (ignored if 'detailed: true' is set)"

.. include:: ../_include/param_basic.rst

Info
****

Get parsed cluster-status.

If 'detailed: false' (*default*) is set - the output from 'crm status full' is used.

Else the output from 'crm status xml' is used.

The 'detailed' output might get updated in the future! (*different modes to filter data and so on*)

Examples
********

.. code-block:: yaml

    - hosts: node1
      gather_facts: false
      become: true
      tasks:
        - name: Example
          ansibleguy.linuxha.status:
            # subset: ['cluster', 'nodes', 'resources', 'operations']
            # time_format: '%Y-%m-%d %H:%M:%S'

        - name: Pulling status
          ansibleguy.linuxha.status:
          register: lha_status

        - name: Showing status
          ansible.builtin.debug:
            var: lha_cnf.data

        # {
        #     "cluster": {
        #         "changed_node": "node1",
        #         "changed_time": "2023-04-02 15:49:30"
        #         "changed_user": "root",
        #         "changed_via": "cibadmin",
        #         "dc": "node1",
        #         "node_count": 2,
        #         "resource_count": 7,
        #         "updated": "2023-04-02 19:29:41"
        #         "version": "2.0.5-ba59be7122"
        #     },
        #     "nodes": {
        #         "node1": {
        #             "resources": {
        #                 "a2": {
        #                     "resource": {
        #                         "class": null,
        #                         "provider": "systemd",
        #                         "type": "apache2.service"
        #                     },
        #                     "state": "Started"
        #                 },
        #                 "ng": {
        #                     "resource": {
        #                         "class": null,
        #                         "provider": "systemd",
        #                         "type": "nginx.service"
        #                     },
        #                     "state": "Started"
        #                 },
        #                 "pingGW": {
        #                     "resource": {
        #                         "class": "ocf",
        #                         "provider": "pacemaker",
        #                         "type": "ping"
        #                     },
        #                     "state": "Started"
        #                 },
        #                 "test2": {
        #                     "resource": {
        #                         "class": "ocf",
        #                         "provider": "heartbeat",
        #                         "type": "IPaddr2"
        #                     },
        #                     "state": "Started"
        #                 }
        #             },
        #             "status": "online"
        #         },
        #         "node2": {
        #             "resources": {
        #                 "a2": {
        #                     "resource": {
        #                         "class": null,
        #                         "provider": "systemd",
        #                         "type": "apache2.service"
        #                     },
        #                     "state": "Started"
        #                 },
        #                 "pingGW": {
        #                     "resource": {
        #                         "class": "ocf",
        #                         "provider": "pacemaker",
        #                         "type": "ping"
        #                     },
        #                     "state": "Started"
        #                 },
        #                 "test1": {
        #                     "resource": {
        #                         "class": "ocf",
        #                         "provider": "heartbeat",
        #                         "type": "IPaddr2"
        #                     },
        #                     "state": "Started"
        #                 }
        #             },
        #             "status": "online"
        #         }
        #     },
        #     "resources": {
        #         "a2": {
        #             "nodes": {
        #                 "node1": "Started",
        #                 "node2": "Started"
        #             },
        #             "resource": {
        #                 "class": null,
        #                 "provider": "systemd",
        #                 "type": "apache2.service"
        #             }
        #         },
        #         "ng": {
        #             "nodes": {
        #                 "node1": "Started"
        #             },
        #             "resource": {
        #                 "class": null,
        #                 "provider": "systemd",
        #                 "type": "nginx.service"
        #             }
        #         },
        #         "pingGW": {
        #             "nodes": {
        #                 "node1": "Started",
        #                 "node2": "Started"
        #             },
        #             "resource": {
        #                 "class": "ocf",
        #                 "provider": "pacemaker",
        #                 "type": "ping"
        #             }
        #         },
        #         "test1": {
        #             "nodes": {
        #                 "node2": "Started"
        #             },
        #             "resource": {
        #                 "class": "ocf",
        #                 "provider": "heartbeat",
        #                 "type": "IPaddr2"
        #             }
        #         },
        #         "test2": {
        #             "nodes": {
        #                 "node1": "Started"
        #             },
        #             "resource": {
        #                 "class": "ocf",
        #                 "provider": "heartbeat",
        #                 "type": "IPaddr2"
        #             }
        #         }
        #     },
        #     "operations": {
        #         "node1": {
        #             "a2": {
        #                 "2023-04-02 15:44:50": {
        #                     "change": "2023-04-02 15:44:50",
        #                     "migration_threshold": "1000000",
        #                     "operation": "probe",
        #                     "operation_id": "128",
        #                     "rc": "0",
        #                     "status": "ok",
        #                     "time_exec": "0ms",
        #                     "time_queue": "0ms"
        #                 }
        #             },
        #             "pingGW": {
        #                 "2023-04-02 15:48:13": {
        #                     "change": "2023-04-02 15:48:13",
        #                     "migration_threshold": "1000000",
        #                     "operation": "start",
        #                     "operation_id": "143",
        #                     "rc": "0",
        #                     "status": "ok",
        #                     "time_exec": "10102ms",
        #                     "time_queue": "0ms"
        #                 }
        #             },
        #             "test1": {
        #                 "2023-04-02 15:33:44": {
        #                     "change": "2023-04-02 15:33:44",
        #                     "migration_threshold": "1000000",
        #                     "operation": "stop",
        #                     "operation_id": "112",
        #                     "rc": "0",
        #                     "status": "ok",
        #                     "time_exec": "17ms",
        #                     "time_queue": "0ms"
        #                 }
        #             }
        #         },
        #         "node2": {
        #             "a2": {
        #                 "2023-04-02 15:44:51": {
        #                     "change": "2023-04-02 15:44:51",
        #                     "migration_threshold": "1000000",
        #                     "operation": "probe",
        #                     "operation_id": "102",
        #                     "rc": "0",
        #                     "status": "ok",
        #                     "time_exec": "0ms",
        #                     "time_queue": "0ms"
        #                 }
        #             }
        #         }
        #     }
        # }

        - name: Pulling detailed status
          ansibleguy.linuxha.status:
            detailed: true
          register: lha_status_detailed

        - name: Showing detailed status
          ansible.builtin.debug:
            var: lha_status_detailed.data

        # {
        #     "node_history": {
        #         "node": {
        #             "name": "node1",
        #             "resource_history": {
        #                 "id": "ANSIBLE_TEST_2_1",
        #                 "migration-threshold": "1000000",
        #                 "operation_history": {
        #                     "call": "245",
        #                     "exec-time": "21ms",
        #                     "last-rc-change": "Sun Apr  2 20:59:51 2023",
        #                     "last-run": "Sun Apr  2 20:59:51 2023",
        #                     "queue-time": "0ms",
        #                     "rc": "0",
        #                     "rc_text": "ok",
        #                     "task": "start"
        #                 },
        #                 "orphan": "false"
        #             }
        #         }
        #     },
        #     "nodes": {
        #         "node": [
        #             {
        #                 "expected_up": "true",
        #                 "id": "1",
        #                 "is_dc": "true",
        #                 "maintenance": "false",
        #                 "name": "node1",
        #                 "online": "true",
        #                 "pending": "false",
        #                 "resources_running": "1",
        #                 "shutdown": "false",
        #                 "standby": "false",
        #                 "standby_onfail": "false",
        #                 "type": "member",
        #                 "unclean": "false"
        #             },
        #             {
        #                 "expected_up": "true",
        #                 "id": "2",
        #                 "is_dc": "false",
        #                 "maintenance": "false",
        #                 "name": "node2",
        #                 "online": "true",
        #                 "pending": "false",
        #                 "resources_running": "0",
        #                 "shutdown": "false",
        #                 "standby": "false",
        #                 "standby_onfail": "false",
        #                 "type": "member",
        #                 "unclean": "false"
        #             }
        #         ]
        #     },
        #     "resources": {
        #         "resource": {
        #             "active": "true",
        #             "blocked": "false",
        #             "failed": "false",
        #             "failure_ignored": "false",
        #             "id": "ANSIBLE_TEST_2_1",
        #             "managed": "true",
        #             "node": {
        #                 "cached": "true",
        #                 "id": "1",
        #                 "name": "node1"
        #             },
        #             "nodes_running_on": "1",
        #             "orphaned": "false",
        #             "resource_agent": "ocf::heartbeat:IPaddr2",
        #             "role": "Started"
        #         }
        #     },
        #     "summary": {
        #         "cluster_options": {
        #             "maintenance-mode": "false",
        #             "no-quorum-policy": "stop",
        #             "stonith-enabled": "false",
        #             "stop-all-resources": "false",
        #             "symmetric-cluster": "true"
        #         },
        #         "current_dc": {
        #             "id": "1",
        #             "name": "node1",
        #             "present": "true",
        #             "version": "2.0.5-ba59be7122",
        #             "with_quorum": "true"
        #         },
        #         "last_change": {
        #             "client": "cibadmin",
        #             "origin": "node1",
        #             "time": "Sun Apr  2 20:59:51 2023",
        #             "user": "root"
        #         },
        #         "last_update": {
        #             "time": "Sun Apr  2 20:59:55 2023"
        #         },
        #         "nodes_configured": {
        #             "number": "2"
        #         },
        #         "resources_configured": {
        #             "blocked": "0",
        #             "disabled": "0",
        #             "number": "1"
        #         },
        #         "stack": {
        #             "type": "corosync"
        #         }
        #     },
        #     "version": "2.0.5"
        # }
