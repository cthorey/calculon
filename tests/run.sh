#!/bin/sh

set -e

header () {
    echo "
###########################################################

$@

###########################################################
"
}

header "Running test suite"
pid="$?"
pytest -s
kill $pid
wait
header "Tests complete"
