#!/usr/bin/env python

from setuptools import setup

setup(name='git-dependencies',
    version='0.1',
    description='Fetch external dependencies from their git repositories and integrate them in the working tree.',
    author='Nico Mandery',
    author_email='nico.mandery@dlr.de',
    scripts=['git-dependencies'],
    install_requires=['PyYAML>=3.0', 'pexpect>=3.1']
)
