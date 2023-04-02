# LinuxHA Tests

## Prerequisites

1. You need two nodes with up-and-running CoroSync + Pacemaker to run the tests!

2. corosync.conf

  * The servers must be configured as 'node1' and 'node2'!
  * The cluster must be named 'linuxha'!

3. Execution

  * You need to create a vars-file that contains the 'ansible_become_pass' and (_if needed_) 'ansible_ssh_pass' variables!
  * Supply the full path to this vars-file to the test-script!
  * The server configured as 'node1' in corosync.conf need to be passed as argument #1 to the test-script!

## Execute

```bash
TEST_NODE1='192.168.0.1'
TEST_NODE2='192.168.0.2'
TEST_SECRETS='/home/guy/.test/linuxha.yml'
COL_PATH=0  # local path to collection to test or 0 to clone from github

bash "${COL_PATH}/scripts/test.sh" "$TEST_NODE1" "$TEST_NODE2" "$TEST_SECRETS" "$COL_PATH"

TEST='raw'  # single test to run
CHECK_MODE=1  # additionally execute test-playbooks in check-mode
bash "${COL_PATH}/scripts/test_single.sh" "$TEST_NODE1" "$TEST_NODE2" "$TEST_SECRETS" "$COL_PATH" "$TEST" "$CHECK_MODE"
```

If you run into any errors - run the '_testenv.yml' tests! They will check your test-environment for basic config-errors!
