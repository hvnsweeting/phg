#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requisites = []

setup(
    name='phg',
    version='1.0.4',
    description='Password hasher and generator',
    scripts=['scripts/phg'],
    long_description=open('README.rst').read(),
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/phg',
    packages=['phg'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
