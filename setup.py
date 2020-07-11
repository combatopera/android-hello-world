from pathlib import Path
from setuptools import Command, find_packages, setup
from threading import Lock
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

def lazy(clazz, init, *initbefore):
    initlock = Lock()
    init = [init]
    def overridefactory(name):
        orig = getattr(clazz, name)
        def override(*args, **kwargs):
            with initlock:
                if init:
                    init[0](obj)
                    del init[:]
            return orig(*args, **kwargs)
        return override
    Lazy = type('Lazy', (clazz, object), {name: overridefactory(name) for name in initbefore})
    obj = Lazy()
    return obj

def cythonize(*args, **kwargs):
    'Allow running apk command with only Python installed.'
    def init(ext_modules):
        from Cython.Build import cythonize
        ext_modules[:] = cythonize(*args, **kwargs)
    return lazy(list, init, '__iter__', '__len__')

setup(
    cmdclass = {'apk': APK},
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize('ahw/**/*.pyx'),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
