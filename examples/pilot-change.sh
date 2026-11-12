#!/usr/bin/env bash
# pilot-change: small example script for Copilot code review pilot
# Adds a~b computation with input validation.

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <int> <int>" >&2
  exit 1
fi

a=$1
b=$2

if ! [[ "$a" =~ ^-?[0-9]+$ ]] || ! [[ "$b" =~ ^-?[0-9]+$ ]]; then
  echo "Error: both arguments must be integers" >&2
  exit 1
fi

echo "a = $a"
echo "b = $b"
echo "a + b = $((a + b))"
echo "a - b = $((a - b))"
echo "a * b = $((a * b))"
