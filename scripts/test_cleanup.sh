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
  NODE1="$1"
  NODE2="$2"
fi

if [ -n "$3" ]
then
  source "$3/bin/activate"
fi

cd "$(dirname "$0")/.."
rm -rf "~/.ansible/collections/ansible_collections/ansibleguy/linuxha"
ansible-galaxy collection install git+https://github.com/ansibleguy/collection_linuxha.git

echo ''
echo 'RUNNING CLEANUP'
echo ''

ansible-playbook tests/cleanup.yml --extra-vars="ansible_python_interpreter=$(which python)" --limit node1 -e ansible_host="$NODE1"
ansible-playbook tests/cleanup.yml --extra-vars="ansible_python_interpreter=$(which python)" --limit node2 -e ansible_host="$NODE2"

rm -rf "~/.ansible/collections/ansible_collections/ansibleguy/linuxha"

echo ''
echo 'FINISHED CLEANUP!'
echo ''
