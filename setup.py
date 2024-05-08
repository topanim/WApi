#!/usr/bin/env python

from io import open
from setuptools import setup, find_packages

"""
:authors: WHAOX
:license: MIT License, see LICENSE file
:copyright: (c) 2024 WHAOX
"""

version = '1.0.29'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whaox-wapi',
    version=version,

    author='WHAOX',
    author_email='gorogannisan641@gmail.com',

    description="Web-Library for Python",
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/topanim/WApi',

    license='MIT LICENSE, see LICENSE file',

    packages=find_packages(),
    install_requires=['jsons', 'requests'],

    keywords=['python', 'web', 'api', 'requests', 'post', 'get']
)
