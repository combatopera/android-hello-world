from setuptools import Command, find_packages, setup # Must precede Cython import.
from Cython.Build import cythonize
from pathlib import Path
import os, subprocess

mirror_volume = 'mirror'
mirror_path = Path('build', 'Cowpox-mirror') # TODO: Do not guess where Cowpox expects it to be.
src_path = '/src'

class APK(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        mirror_path.mkdir(parents = True, exist_ok = True)
        subprocess.check_call([
            'docker', 'run', '--rm', '-it',
            '-v', f"{Path.cwd()}:{src_path}",
            '-v', f"{mirror_volume}:{src_path}/{str(mirror_path).replace(os.sep, '/')}",
            'combatopera/cowpox', src_path,
        ])

setup(
    cmdclass = {'apk': APK},
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize('ahw/**/*.pyx'),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
