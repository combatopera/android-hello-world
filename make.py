#!/usr/bin/env python3

from pathlib import Path
import os

mirror_volume = Path.home() / '.Cowpox' / 'mirror'
mirror_relpath = Path('build', 'Cowpox-mirror') # TODO: Do not guess where Cowpox expects it to be.
src_path = '/src'

def main():
    'Example for building the APK.'
    for d in mirror_volume, mirror_relpath:
        d.mkdir(parents = True, exist_ok = True)
    command = [
        'docker', 'run', '--rm', '-it',
        '-v', f"{Path.cwd()}:{src_path}",
        '-v', f"{mirror_volume}:{src_path}/{str(mirror_relpath).replace(os.sep, '/')}",
        'combatopera/cowpox', src_path,
    ]
    os.execvp(command[0], command)

if '__main__' == __name__:
    main()
