# Ansible Collection - ansibleguy.linuxha

[![Functional Test Status](https://badges.ansibleguy.net/linuxha.collection.test.svg)](https://github.com/ansibleguy/collection_linuxha/blob/latest/scripts/test.sh)
[![Lint Test Status](https://badges.ansibleguy.net/linuxha.collection.lint.svg)](https://github.com/ansibleguy/collection_linuxha/blob/latest/scripts/lint.sh)
[![Docs](https://readthedocs.org/projects/ansible-linuxha/badge/?version=latest&style=flat)](https://linuxha.ansibleguy.net)
[![Ansible Galaxy](https://img.shields.io/ansible/collection/2409)](https://galaxy.ansible.com/ansibleguy/linuxha)

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

Example config: [documentation](https://linuxha.ansibleguy.net/en/latest/usage/config.html)

### XML Parsing

The [xmltodict python module](https://github.com/martinblech/xmltodict) is used to parse config!

It is only needed on the Ansible controller!

```bash
python3 -m pip install xmltodict
```

### Collection

Then - install the collection itself:

```bash
# stable/tested version:
ansible-galaxy collection install ansibleguy.linuxha

# latest version:
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git

# install to specific directory for easier development
cd $PLAYBOOK_DIR
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git -p ./collections
```

----

## Usage

See: [Docs](https://linuxha.ansibleguy.net)

----

## Modules

**Development States**:

not implemented => development => [testing](https://github.com/ansibleguy/collection_linuxha/tree/latest/tests) => unstable (_practical testing_) => stable

### Implemented


| Function                 | Module                    | Usage                                                                | State    |
|:-------------------------|:--------------------------|:---------------------------------------------------------------------|:---------|
| **Execute raw commands** | ansibleguy.linuxha.raw    | [Docs](https://linuxha.ansibleguy.net/en/latest/modules/raw.html)    | unstable |
| **Parsed status**        | ansibleguy.linuxha.status | [Docs](https://linuxha.ansibleguy.net/en/latest/modules/status.html) | unstable |
| **Parsed config**        | ansibleguy.linuxha.config | [Docs](https://linuxha.ansibleguy.net/en/latest/modules/config.html) | unstable  |

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
