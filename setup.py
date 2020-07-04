from Cython.Build import cythonize
from pathlib import Path
from setuptools import find_packages, setup

setup(
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize(str(Path('ahw', 'native.pyx'))),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
