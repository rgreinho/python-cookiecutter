#!/bin/bash

set -euo pipefail

test -z "$(yapf -d -r processor)"
