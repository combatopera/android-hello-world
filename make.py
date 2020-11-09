#!/usr/bin/env python3

from pathlib import Path
import os

host_mirror = Path.home() / '.Cowpox' / 'mirror'
container_mirror = '/mirror'
container_src = '/src'

def main():
    'Example for building the APK.'
    host_mirror.mkdir(parents = True, exist_ok = True)
    command = [
        'docker', 'run', '--rm', '-it',
        '-v', f"{Path.cwd()}:{container_src}",
        '-v', f"{host_mirror}:{container_mirror}",
        'combatopera/cowpox',
        '--mirror', container_mirror,
        container_src,
    ]
    os.execvp(command[0], command)

if '__main__' == __name__:
    main()
