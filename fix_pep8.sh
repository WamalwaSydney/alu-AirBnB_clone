#!/usr/bin/env bash
set -e

# Install autopep8 if missing (user install)
if ! python3 -m autopep8 --version &>/dev/null; then
    echo "autopep8 not found, installing..."
    python3 -m pip install --user autopep8
fi

# Reformat console.py
python3 -m autopep8 --in-place --aggressive --aggressive console.py

# Reformat model files
python3 -m autopep8 --in-place --aggressive --aggressive models/*.py

# Reformat engine files
python3 -m autopep8 --in-place --aggressive --aggressive models/engine/*.py

# Reformat tests recursively
autopep8_args="--in-place --aggressive --aggressive"
find tests -name "*.py" -exec python3 -m autopep8 $autopep8_args {} +

echo "✅ All Python files have been auto-formatted with autopep8."

