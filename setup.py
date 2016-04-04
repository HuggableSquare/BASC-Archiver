#!/usr/bin/env python
# coding: utf-8
import codecs
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with codecs.open('README.rst') as file:
    long_description = file.read()
    if not isinstance(long_description, str):
        long_description = str(long_description, 'utf-8')


setup(
    name='BASC-Archiver',
    version='0.9.7',
    description='Makes a complete archive of imageboard threads including images, HTML, and JSON.',
    long_description=long_description,
    author='Lawrence Wu <sagnessagiel@gmail.com>, Daniel Oaks <daniel@danieloaks.net>',
    author_email='sagnessagiel@gmail.com',
    url='https://github.com/bibanon/BASC-Archiver',
    scripts=['thread-archiver', '4chan-thread-archiver', 'archive-nabber'],
    packages=['basc_archiver', 'basc_archiver.sites'],
    package_dir={
        'basc_archiver': 'basc_archiver',
        'basc_archiver.sites': 'basc_archiver/sites',
    },
    package_data = {
        'basc_archiver.sites': ['templates/*']
    },
    install_requires=['requests', 'docopt>=0.5.0', 'BASC-py4chan>=0.5.5', 'jinja2', 'django-htmlmin'],
    keywords='4chan downloader images json dump',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
