from setuptools import find_packages, setup
import Cython.Build

setup(
    entry_points = {'console_scripts': ['android-hello=ahw:main']},
    ext_modules = Cython.Build.cythonize('ahw/**/*.pyx', compiler_directives = {'language_level': 3}),
    install_requires = ['Kivy'], # TODO: Use specific version.
    name = 'android-hello-world',
    packages = find_packages(),
)
