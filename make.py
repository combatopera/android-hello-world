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
        f"container src = {container_src}",
        f"container mirror = {container_mirror}",
    ]
    os.execvp(command[0], command)

if '__main__' == __name__:
    main()
