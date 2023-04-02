#!/usr/bin/env bash

set -e

echo ''

if [ -z "$1" ] || [ -z "$2" ]
then
  echo 'Arguments:'
  echo '  1: test-server #1'
  echo '  2: test-server #2'
  echo '  3: path to virtual environment (optional)'
  echo ''
  exit 1
else
  TEST_NODE1="$1"
  TEST_NODE2="$2"
fi

if [ -n "$3" ]
then
  source "$3/bin/activate"
fi

cd "$(dirname "$0")/.."
rm -rf "~/.ansible/collections/ansible_collections/ansibleguy/linuxha"
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git

TMPL_HOST_VARS="---\n\nansible_host:"
echo -e "$TMPL_HOST_VARS '$TEST_NODE1'" > "$TMP_HOST_VARS/node1.yml"
echo -e "$TMPL_HOST_VARS '$TEST_NODE2'" > "$TMP_HOST_VARS/node2.yml"

echo ''
echo 'RUNNING CLEANUP'
echo ''

ansible-playbook tests/_cleanup.yml -i tests/inv/hosts.yml $VERBOSITY

rm -rf "~/.ansible/collections/ansible_collections/ansibleguy/linuxha"

echo ''
echo 'FINISHED CLEANUP!'
echo ''
