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

    mirror_volume = Path.home() / '.Cowpox' / 'mirror'
    mirror_relpath = Path('build', 'Cowpox-mirror') # TODO: Do not guess where Cowpox expects it to be.
    src_path = '/src'

    def run(self):
        for d in self.mirror_volume, self.mirror_relpath:
            d.mkdir(parents = True, exist_ok = True)
        subprocess.check_call([
            'docker', 'run', '--rm', '-it',
            '-v', f"{Path.cwd()}:{self.src_path}",
            '-v', f"{self.mirror_volume}:{self.src_path}/{str(self.mirror_relpath).replace(os.sep, '/')}",
            'combatopera/cowpox', self.src_path,
        ])

class cythonize(list):

    class Guard: pass

    def __init__(self, *args, **kwargs):
        super().__init__([self.Guard()])
        self.args = args
        self.kwargs = kwargs

    def _populate(self):
        from Cython.Build import cythonize
        self[:] = cythonize(*self.args, **self.kwargs)
        self._populate = lambda: None

    def __iter__(self):
        self._populate()
        return super().__iter__()

setup(
    cmdclass = {'apk': APK},
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize('ahw/**/*.pyx'),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
