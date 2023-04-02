.. _usage_config:

.. include:: ../_include/head.rst

==========
2 - Config
==========

**Docs**: `corosync.conf <https://manpages.debian.org/testing/corosync/corosync.conf.5.en.html>`_

Example
*******

.. code-block::

    totem {
      version: 2
      cluster_name: clusterName

      knet_transport: udp
      transport: knet

      # generate key: corosync-keygen -k /etc/corosync/authkey_clusterName
      # all nodes in the cluster must share the same key
      keyfile: /etc/corosync/authkey_clusterName
      crypto_cipher: aes256
      crypto_hash: sha256
      secauth: yes

      link_mode: passive
      # passive, active, rr
      netmtu: 1500
      ip_version: ipv4
      # ipv4, ipv6, ipv4-6

      interface {
        ringnumber: 0
        bindnetaddr: 192.168.1.0
        # network-address of subnet
        mcastport: 5405
        # +2 for next cluster
      }
      interface {
        ringnumber: 1
        bindnetaddr: 10.0.0.0
        # network-address of subnet
        mcastport: 5405
        # +2 for next cluster
      }

    }

    logging {
      # debugging
      debug: off
      fileline: off
      function_name: off
      #timestamp: hires

      to_stderr: yes
      to_syslog: yes
      syslog_facility: daemon
      syslog_priority: info
      # alert, crit, debug (same as debug = on), emerg, err, info, notice, warning

      logger_subsys {
        subsys: QUORUM
        debug: off
      }
    }

    quorum {
      provider: corosync_votequorum
    }

    nodelist {
      node {
        name: node1
        nodeid: 1
        ring0_addr: 192.168.1.1
        # private ip
        ring1_addr: 10.0.0.1
        # public ip
      }
      node {
        name: node2
        nodeid: 2
        ring0_addr: 192.168.1.2
        # private ip
        ring1_addr: 10.0.0.2
        # public ip
      }
    }

    system {}
    nozzle {}

Testing
*******

.. code-block:: bash

    root@lha01:~# corosync -f
    > parse error in config: ...

Starting
********

.. code-block:: bash

    root@lha01:~# systemctl enable corosync.service
    root@lha01:~# systemctl enable pacemaker.service
    root@lha01:~# systemctl start corosync.service
    root@lha01:~# systemctl start pacemaker.service

Checking
********

.. code-block:: bash

    root@lha01:~# systemctl status corosync.service
    > ● corosync.service - Corosync Cluster Engine
    >      Loaded: loaded (/lib/systemd/system/corosync.service; enabled; vendor preset: enabled)
    >      Active: active (running) since Sat 2023-04-01 16:30:46 CEST; 9min ago

    root@lha01:~# systemctl status pacemaker.service
    > ● pacemaker.service - Pacemaker High Availability Cluster Manager
    >      Loaded: loaded (/lib/systemd/system/pacemaker.service; enabled; vendor preset: enabled)
    >      Active: active (running) since Sat 2023-04-01 16:31:05 CEST; 9min ago

    root@lha01:~# crm status
    > Cluster Summary:
    >   * Stack: corosync
    >   * Current DC: lha02 (version 2.0.5-ba59be7122) - partition with quorum
    >   * Last updated: Sat Apr  1 16:31:39 2023
    >   * Last change:  Sat Apr  1 16:31:11 2023 by hacluster via crmd on lha02
    >   * 2 nodes configured
    >   * 0 resource instances configured
    >
    > Node List:
    >   * Online: [ lha01 lha02 ]
    >
    > Full List of Resources:
    >   * No resources


