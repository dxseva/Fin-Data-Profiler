#!/usr/bin/env python3
import os

try:
    venv_path = os.environ['VIRTUAL_ENV']
    print(f"Your current virtual env is {venv_path}")
except KeyError:
    print("No virtual environment is active.")
