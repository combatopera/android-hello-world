#!/usr/bin/env python3

from pathlib import Path
import os

host_mirror = Path.home() / '.Cowpox' / 'mirror'
mirror_relpath = Path('build', 'Cowpox-mirror')
container_src = '/src'

def main():
    'Example for building the APK.'
    for d in host_mirror, mirror_relpath:
        d.mkdir(parents = True, exist_ok = True)
    command = [
        'docker', 'run', '--rm', '-it',
        '-v', f"{Path.cwd()}:{container_src}",
        '-v', f"{host_mirror}:{container_src}/{str(mirror_relpath).replace(os.sep, '/')}",
        'combatopera/cowpox',
        f"container src = {container_src}",
        f"mirror path = {container_src}/{str(mirror_relpath).replace(os.sep, '/')}",
    ]
    os.execvp(command[0], command)

if '__main__' == __name__:
    main()
