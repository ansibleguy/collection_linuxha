#!/usr/bin/env bash

set -e

echo ''

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]
then
  echo 'Arguments:'
  echo '  1: test-server #1'
  echo '  2: test-server #2'
  echo '  3: path to secret-vars-file (ansible_become_pass)'
  echo "  4: path to local collection - set to '0' to clone from github"
  echo '  5: path to virtual environment (optional)'
  echo ''
  exit 1
else
  TEST_NODE1="$1"
  TEST_NODE2="$2"
fi

export TEST_SECRETS="$3"
LOCAL_COLLECTION="$4"

if [ -n "$5" ]
then
  source "$5/bin/activate"
fi

set -u

source "$(dirname "$0")/test_prep.sh"  # shared

echo ''
echo 'RUNNING CLEANUP'
echo ''

ansible-playbook tests/_cleanup.yml -i tests/inv/hosts.yml

rm -rf "$TMP_DIR"

echo ''
echo 'FINISHED CLEANUP!'
echo ''
