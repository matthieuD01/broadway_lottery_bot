#!/usr/bin/env bash
set -e

# Load variables from .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

if [ -z "$CONDA_ENV" ]; then
    echo "CONDA_ENV not specified in .env" >&2
    exit 1
fi

CONDA_BASE=$(conda info --base)
source "$CONDA_BASE/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV"

python main.py
