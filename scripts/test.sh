#!/usr/bin/env bash

set -eo pipefail

echo ''

DEBUG=false
export ANSIBLE_HOST_KEY_CHECKING=False

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

if [[ "$DEBUG" == true ]]
then
  VERBOSITY='-D -vvv'
else
  VERBOSITY=''
fi

set -u

source "$(dirname "$0")/test_prep.sh"  # shared between single/multi test

echo ''
echo '##############################'
echo 'STARTING TESTS!'
echo '##############################'
echo ''

run_test '_testenv' 0
run_test 'base' 0
run_test 'raw' 1
run_test 'status' 1
run_test 'config' 1

echo ''
echo '##############################'
echo 'FINISHED TESTS!'
echo '##############################'
echo ''

rm -rf "$TMP_DIR"
