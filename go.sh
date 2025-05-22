#!/bin/bash

DIR0=$(dirname "$0")
main() {
  pipenv run python ./connect.py "$@"
}
cd "$DIR0" && main "$@"
