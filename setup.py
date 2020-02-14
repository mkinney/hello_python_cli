from setuptools import setup

from io import open

import tomlkit


def _get_version():
    with open('pyproject.toml') as pyproject:
        file_contents = pyproject.read()
    return tomlkit.parse(file_contents)['project']['version']


with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
   name='hello_python_cli',
   version=_get_version(),
   description='Simple python hello cli program',
   long_description=readme,
   long_description_content_type='text/markdown',
   author='Mike Kinney',
   author_email='mike.kinney@gmail.com',
   packages=['hello_module'],
   install_requires=[('docopt', 'tomlkit')],
   scripts=['hello'],
)
