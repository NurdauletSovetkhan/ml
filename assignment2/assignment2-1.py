import sys
import numpy as np
import pandas as pd

REQUIRED = {
    'numpy': '2.4.3',
    'pandas': '3.0.1'
}

installed = {
    'numpy': '2.4.3',
    'pandas': '3.0.1'
}

print(f'Python: {sys.version.split()[0]}')
print('=' * 45)

issues = 0
for lib, min_ver in REQUIRED.items():
    ver = REQUIRED[lib]
    status = 'OK' if ver >= min_ver else 'OUTDATED'
    print(f' {lib:8s} installed: {ver:10s} required: {min_ver:6s} [{status}] ')
    if status != 'OK':
        print(status)

print('=' * 45)
if issues == 0:
    print('Everything is alrighty')
else:
    print(f'WARNING: {issues} libraries/library need updating ')
    