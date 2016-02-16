#!/usr/bin/env python

from setuptools import setup

setup(name='git-dependencies',
    version='0.2.0',
    description='Fetch external dependencies from their git repositories and integrate them in the working tree.',
    author='Nico Mandery',
    author_email='nico.mandery@dlr.de',
    scripts=['git-dependencies'],
    install_requires=['PyYAML>=3.0', 'pexpect>=3.1'],
    url="http://git.ukis.eoc.dlr.de/projects/ADMIN/repos/git-dependencies/browse"
)
