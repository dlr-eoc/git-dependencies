#!/usr/bin/env python

from setuptools import setup
import codecs
import os
import re

def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(name='git-dependencies',
    version=find_version('git-dependencies'),
    description='Fetch external dependencies from their git repositories and integrate them in the working tree.',
    author='Nico Mandery',
    author_email='nico.mandery@dlr.de',
    scripts=['git-dependencies'],
    install_requires=['PyYAML>=3.0', 'pexpect>=3.1'],
    url="http://git.ukis.eoc.dlr.de/projects/ADMIN/repos/git-dependencies",
    license='Apache License 2.0',
)
