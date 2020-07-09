from pathlib import Path
from setuptools import Command, find_packages, setup
from warnings import warn
import os, subprocess

class APK(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    mirror_volume = 'mirror'
    mirror_path = Path('build', 'Cowpox-mirror') # TODO: Do not guess where Cowpox expects it to be.
    src_path = '/src'

    def run(self):
        self.mirror_path.mkdir(parents = True, exist_ok = True)
        subprocess.check_call([
            'docker', 'run', '--rm', '-it',
            '-v', f"{Path.cwd()}:{self.src_path}",
            '-v', f"{self.mirror_volume}:{self.src_path}/{str(self.mirror_path).replace(os.sep, '/')}",
            'combatopera/cowpox', self.src_path,
        ])

def cythonize(*args, **kwargs):
    try:
        from Cython.Build import cythonize
    except ModuleNotFoundError:
        warn('Cython not available, ext_modules left blank.')
        return []
    return cythonize(*args, **kwargs)

setup(
    cmdclass = {'apk': APK},
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize('ahw/**/*.pyx'),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
