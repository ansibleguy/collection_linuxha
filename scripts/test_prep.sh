#!/usr/bin/env bash

set -u

TMP_DIR="/tmp/.linuxha_test_$(date +%s)"
TMP_COL_DIR="$TMP_DIR/collections"
TMP_COL_DIR2="$TMP_COL_DIR/ansible_collections/ansibleguy/linuxha"
TMP_HOST_VARS="$TMP_COL_DIR2/tests/inv/host_vars"
TMPL_HOST_VARS="---\n\nansible_host:"

mkdir -p "$TMP_COL_DIR"
cd "$TMP_DIR"
export ANSIBLE_COLLECTIONS_PATH="$TMP_COL_DIR"

if [[ "$LOCAL_COLLECTION" == '0' ]]
then
  ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git -p "$TMP_COL_DIR"
else
  if [ -d "$LOCAL_COLLECTION" ]
  then
    echo "### TESTING COLLECTION: '$LOCAL_COLLECTION' ###"
    mkdir -p "$TMP_COL_DIR/ansible_collections/ansibleguy/"
    ln -s "$LOCAL_COLLECTION" "$TMP_COL_DIR/ansible_collections/ansibleguy/"
  else
    echo "Provided collection path does not exist: '$LOCAL_COLLECTION'"
    exit 1
  fi
fi

echo -e "$TMPL_HOST_VARS '$TEST_NODE1'" > "$TMP_HOST_VARS/node1.yml"
echo -e "$TMPL_HOST_VARS '$TEST_NODE2'" > "$TMP_HOST_VARS/node2.yml"

function run_test() {
  module="$1"
  check_mode="$2"

  echo ''
  echo '##############################'
  echo "RUNNING TESTS of module: '$module'"
  echo ''

  ansible-playbook "tests/$module.yml" -i tests/inv/hosts.yml $VERBOSITY
  if [[ "$check_mode" == '1' ]]
  then
    ansible-playbook "tests/$module.yml" -i tests/inv/hosts.yml --check $VERBOSITY
  fi
}

cd "$TMP_COL_DIR2"
