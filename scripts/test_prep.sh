#!/usr/bin/env bash

set -u

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

function run_test() {
  module="$1"
  check_mode="$2"

  echo ''
  echo '##############################'
  echo "RUNNING TESTS of module: '$module'"
  echo ''

  ansible-playbook "tests/$module.yml" -i tests/_inventory.yml -e ansible_host="$TEST_NODE1" --limit node1 $VERBOSITY
  ansible-playbook "tests/$module.yml" -i tests/_inventory.yml -e ansible_host="$TEST_NODE2" --limit node2 $VERBOSITY
  if [[ "$check_mode" == '1' ]]
  then
    ansible-playbook "tests/$module.yml" -i tests/_inventory.yml -e ansible_host="$TEST_NODE1" --limit node1 --check $VERBOSITY
    ansible-playbook "tests/$module.yml" -i tests/_inventory.yml -e ansible_host="$TEST_NODE2" --limit node2 --check $VERBOSITY
  fi
}
