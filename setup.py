from pathlib import Path
from setuptools import Command, find_packages, setup
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from zipfile import ZipFile
import os, shutil, subprocess

# Lazy cythonize to allow running apk command with only Python installed:
with NamedTemporaryFile() as g:
    with urlopen('https://files.pythonhosted.org/packages/dd/22/f5573c59f64f935c7153b58f1ceeaa1938cf8d22f71950d64fc56e148db7/pyven-44-py2.py3-none-any.whl') as f:
        shutil.copyfileobj(f, g)
    with ZipFile(g.name) as zf, zf.open('pyven/cythonize.py') as f:
        exec(f.read())

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

setup(
    cmdclass = {'apk': APK},
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize('ahw/**/*.pyx'),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
