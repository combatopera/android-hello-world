#!/usr/bin/env python3

from pathlib import Path
import os

mirror_volume = Path.home() / '.Cowpox' / 'mirror'
mirror_relpath = Path('build', 'Cowpox-mirror')
container_path = '/src'

def main():
    'Example for building the APK.'
    for d in mirror_volume, mirror_relpath:
        d.mkdir(parents = True, exist_ok = True)
    command = [
        'docker', 'run', '--rm', '-it',
        '-v', f"{Path.cwd()}:{container_path}",
        '-v', f"{mirror_volume}:{container_path}/{str(mirror_relpath).replace(os.sep, '/')}",
        'combatopera/cowpox',
        f"container src = {container_path}",
        f"mirror path = {container_path}/{str(mirror_relpath).replace(os.sep, '/')}",
    ]
    os.execvp(command[0], command)

if '__main__' == __name__:
    main()
