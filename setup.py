#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import codecs

PACKAGE_NAME = 'pyspartaproj'
EMAIL = 'lyouta@spartaproject.com'
AUTHOR_NAME = 'lyouta'
SEARCH_KEYWORDS = 'sparta spartaproject pyspartaproj'
PACKAGE_VERSION = '0.0.1'
PACKAGE_DESCRIPTION = 'spartaproject'
PRODUCT_URL = 'https://github.com/lyoutakoduka'
CONTENT_TYPE = 'text/markdown'
LICENSE_TYPE = 'MIT'

README_PATH = 'README.md'

INSTALL_REQUIRES = [
    'PySide6>=6.4.3',
    'PyOpenGL>=3.1.6',
    'numpy>=1.24.2']

CLASSIFIERS = [
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
    'Topic :: Multimedia :: Graphics :: 3D Modeling']

ENCODING_TYPE = 'utf-8'

with codecs.open(PACKAGE_NAME, encoding=ENCODING_TYPE) as file:
    long_description = file.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=PACKAGE_DESCRIPTION,
    long_description=long_description,
    long_description_content_type=CONTENT_TYPE,
    url=PRODUCT_URL,
    author=AUTHOR_NAME,
    author_email=EMAIL,
    license=LICENSE_TYPE,
    keywords=SEARCH_KEYWORDS,
    packages=[PACKAGE_NAME],
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS)
