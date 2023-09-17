#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open

from setuptools import setup

_PACKAGE_NAME = 'pyspartaproj'
_EMAIL = 'lyouta@spartaproject.com'
_AUTHOR_NAME = 'lyouta'
_SEARCH_KEYWORDS = 'sparta spartaproject pyspartaproj'
_PACKAGE_VERSION = '0.0.1'
_PACKAGE_DESCRIPTION = 'spartaproject'
_PRODUCT_URL = 'https://github.com/lyoutakoduka'
_CONTENT_TYPE = 'text/markdown'
_LICENSE_TYPE = 'MIT'

_README_PATH = 'README.md'

_INSTALL_REQUIRES = [
    'PySide6>=6.4.3',
    'PyOpenGL>=3.1.6',
    'numpy>=1.24.2'
]

_CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: GPU',
    'Environment :: X11 Applications :: Qt',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: C++',
    'Topic :: Artistic Software',
    'Topic :: Multimedia :: Graphics :: 3D Modeling'
]

_ENCODING_TYPE = 'utf-8'


with open(_README_PATH, encoding=_ENCODING_TYPE) as file:
    long_description = file.read()

setup(
    name=_PACKAGE_NAME,
    version=_PACKAGE_VERSION,
    description=_PACKAGE_DESCRIPTION,
    long_description=long_description,
    long_description_content_type=_CONTENT_TYPE,
    url=_PRODUCT_URL,
    author=_AUTHOR_NAME,
    author_email=_EMAIL,
    license=_LICENSE_TYPE,
    keywords=_SEARCH_KEYWORDS,
    packages=[_PACKAGE_NAME],
    install_requires=_INSTALL_REQUIRES,
    classifiers=_CLASSIFIERS
)
