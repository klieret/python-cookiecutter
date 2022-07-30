#!/usr/bin/env bash

# bash strict mode
set -euo pipefail
IFS=$'\n\t'

git init
pre-commit install
gitmoji -i
