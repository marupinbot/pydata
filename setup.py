#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydata',
    version='0.0.1',
    description='PyData Location List',
    long_description=long_description,
    url='https://github.com/takezyou/pydata',
    author='takezyou',
    author_email='kaitokun07@icloud.com',
    license='MIT',
    install_requires=['beautifulsoup4'],
    keywords='pydata',
    packages=find_packages(exclude=('tests')),
    entry_points={
        "console_scripts": [
            "pydata=pydata.__init__:main",
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)