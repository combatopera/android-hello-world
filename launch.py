#!/usr/bin/env python3

from pathlib import Path
import os, subprocess, venv

env_dir = Path('env')

def main():
    'Example for testing the app locally.'
    bin_dir = env_dir / 'bin'
    command = [bin_dir / 'android-hello']
    if not command[0].exists():
        assert not env_dir.exists()
        venv.create(env_dir, with_pip = True)
        install = lambda *args: subprocess.check_call([bin_dir / 'pip', 'install', *args])
        install('--upgrade', 'pip')
        install('--editable', '.') # XXX: Can we make native.pyx editable too?
    os.execv(command[0], command)

if '__main__' == __name__:
    main()
