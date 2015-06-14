# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup, find_packages

VERSION = (0, 0, 2)
__version__ = VERSION
__versionstr__ = '.'.join([str(v) for v in VERSION])

install_requires = ['beautifulsoup4>=4.3', 'requests>=2.7']
test_require = install_requires + ['coverage>=3.7', 'nose>=1.3', 'responses']

setup(
    name='python-opengraph',
    version=__versionstr__,
    description='Python module to parse Open Graph metadata on web pages',
    url='https://github.com/HenrikOssipoff/python-opengraph',
    license='MIT',
    author='Henrik Ossipoff Hansen',
    author_email='henrik.ossipoff@gmail.com',
    install_requires=install_requires,
    packages=find_packages(exclude=['tests']),
    tests_require=test_require,
    test_suite='tests.run_tests.all',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ])
