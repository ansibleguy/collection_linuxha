# Ansible Collection - ansibleguy.linuxha

[![Lint](https://github.com/ansibleguy/collection_linuxha/actions/workflows/lint.yml/badge.svg)](https://github.com/ansibleguy/collection_linuxha/actions/workflows/lint.yml)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/repo/published/ansibleguy/linuxha)

**Functional Tests**: 

* Status: [![Functional Test Status](https://badges.ansibleguy.net/linuxha.collection.test.svg)](https://github.com/ansibleguy/collection_linuxha/blob/latest/scripts/test.sh) |
[![Functional-Tests](https://github.com/ansibleguy/collection_linuxha/actions/workflows/functional_test_result.yml/badge.svg)](https://github.com/ansibleguy/collection_linuxha/actions/workflows/functional_test_result.yml)
* Logs: [API](https://ci.ansibleguy.net/api/job/ansible-test-collection-linuxha/logs?token=2b7bba30-9a37-4b57-be8a-99e23016ce70&lines=1000) |
[Daily Archive](https://github.com/ansibleguy/collection_linuxha/actions/workflows/functional_test_result.yml) |
[Short](https://badges.ansibleguy.net/log/collection_linuxha_test_short.log) | [Full](https://badges.ansibleguy.net/log/collection_linuxha_test.log)

Internal CI: [Tester Role](https://github.com/ansibleguy/_meta_cicd) | [Jobs API](https://github.com/O-X-L/github-self-hosted-jobs-systemd)

----

## Contribute

Feel free to contribute to this project using [pull-requests](https://github.com/ansibleguy/collection_linuxha/pulls), [issues](https://github.com/ansibleguy/collection_linuxha/issues) and [discussions](https://github.com/ansibleguy/collection_linuxha/discussions)!

**What to contribute**:

* add ansible-based [tests](https://github.com/ansibleguy/collection_linuxha/blob/latest/tests) for some error-case(s) you have encountered
* extend or correct the [documentation](https://github.com/ansibleguy/collection_linuxha/blob/latest/docs)
* contribute code fixes or optimizations
* implement additional modules
* test unstable modules and report bugs/errors

----

## Requirements

### LinuxHA

You will have to install the LinuxHA packages on the target server:
* [LinuxHA](https://wiki.clusterlabs.org/wiki/Install) ([corosync](https://github.com/corosync/corosync) and [pacemaker](https://github.com/ClusterLabs/pacemaker))
* [crm-shell](https://github.com/ClusterLabs/crmsh) (crmsh)

After that - configure the basic cluster using the '[corosync.conf](https://linux.die.net/man/5/corosync.conf)' file.

Example config: [documentation](https://linuxha.ansibleguy.net/usage/config.html)

### XML Parsing

The [xmltodict python module](https://github.com/martinblech/xmltodict) is used to parse config!

It is only needed on the Ansible controller!

```bash
python3 -m pip install xmltodict
```

### Collection

Then - install the collection itself:

```bash
# latest version:
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git

# stable/tested version:
ansible-galaxy collection install ansibleguy.linuxha

# install to specific directory for easier development
cd $PLAYBOOK_DIR
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git -p ./collections
```

----

## Advertisement

* Need **professional support** using Ansible or LinuxHA? Contact us:

  E-Mail: [contact@oxl.at](mailto:contact@oxl.at)

  Tel: [+43 3115 40 900 0](tel:+433115409000)

  Web: [EN](https://www.o-x-l.com) | [DE](https://www.oxl.at)

  Language: German or English

* You want a simple **Ansible GUI**?

  Check-out this [Ansible WebUI](https://github.com/ansibleguy/webui)

----

## Usage

See: [Docs](https://linuxha.ansibleguy.net)

[![Docs Uptime](https://status.oxl.at/api/v1/endpoints/4--ansibleguy_ansible-collection---linuxha-documentation/uptimes/7d/badge.svg)](https://status.oxl.at/endpoints/4--ansibleguy_ansible-collection---linuxha-documentation)

[Alternative Link](https://ansible-linuxha.readthedocs.io/)

----

## Modules

**Development States**:

not implemented => development => [testing](https://github.com/ansibleguy/collection_linuxha/tree/latest/tests) => unstable (_practical testing_) => stable

### Implemented


| Function                 | Module                    | Usage                                                                | State    |
|:-------------------------|:--------------------------|:---------------------------------------------------------------------|:---------|
| **Execute raw commands** | ansibleguy.linuxha.raw    | [Docs](https://linuxha.ansibleguy.net/modules/raw.html)    | unstable |
| **Parsed status**        | ansibleguy.linuxha.status | [Docs](https://linuxha.ansibleguy.net/modules/status.html) | unstable |
| **Parsed config**        | ansibleguy.linuxha.config | [Docs](https://linuxha.ansibleguy.net/modules/config.html) | unstable  |

### Roadmap

- Status
  - Current config
  - Cluster status
  - Cluster health
- Actions
  - [Resource Actions](https://crmsh.github.io/man-2.0/#cmdhelp_resource)
  - [Node Actions](https://crmsh.github.io/man-2.0/#cmdhelp_node)
- [Configuration](https://crmsh.github.io/man-2.0/#cmdhelp_configure)
  - [Property](https://crmsh.github.io/man-2.0/#cmdhelp_configure_property)
  - [Primitives](https://crmsh.github.io/man-2.0/#cmdhelp_configure_primitive)
  - [Monitor](https://crmsh.github.io/man-2.0/#cmdhelp_configure_monitor)
  - [Clone](https://crmsh.github.io/man-2.0/#cmdhelp_configure_clone)
  - [Groups](https://crmsh.github.io/man-2.0/#cmdhelp_configure_group)
  - [Order](https://crmsh.github.io/man-2.0/#cmdhelp_configure_order)
  - [Location](https://crmsh.github.io/man-2.0/#cmdhelp_configure_location)
  - [Co-Location](https://crmsh.github.io/man-2.0/#cmdhelp_configure_colocation)
  - [Master-Slave](https://crmsh.github.io/man-2.0/#cmdhelp_configure_ms)
