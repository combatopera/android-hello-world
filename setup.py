from setuptools import find_packages, setup
from Cython.Build import cythonize

setup(
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = cythonize('ahw/**/*.pyx', compiler_directives = {'language_level': 3}),
    install_requires = ['Kivy>=2'],
    name = 'android-hello-world',
    packages = find_packages(),
)
