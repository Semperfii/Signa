#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

setup(
    name='signa',
    version='0.1.0',
    license='BSD',
    description='The web package for signa.',
    long_description='The web package for signa.',
    author='Alexis *fuego* Tacnet',
    author_email='alexistacnet@gmail.com',
    url='https://github.com/fuegowolf/signa',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[],
    install_requires=[
        'Flask==0.12.2',
        'Flask-Cors==3.0.3',
        'Flask-RESTful==0.3.6',
        'peewee==3.0.16',
        'psycopg2-binary==2.7.4',
        'Flask-JWT-Extended==3.7.0',
        'requests==2.18.4',
        'Flask-OAuthlib==0.9.4'
    ],
    extras_require={},
    entry_points='''
        [console_scripts]
        signa=cli:cli
    '''
)
