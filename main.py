import os
import shutil

MAKEFUN_OUTPUT_DIR = os.getenv('MAKEFUN_OUTPUT_DIR', '/output')

if not os.path.exists(MAKEFUN_OUTPUT_DIR):
    os.makedirs(MAKEFUN_OUTPUT_DIR)

shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entry.png'), os.path.join(MAKEFUN_OUTPUT_DIR, 'entry.png'))

print('entry.png copied to', MAKEFUN_OUTPUT_DIR)

# MAKEFUN_OUTPUT_DIR=out python3 main.py
