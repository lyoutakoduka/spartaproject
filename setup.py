# -*- coding: utf-8 -*-

import setuptools
import codecs
import os

package_name = 'pyspartaproj'

INSTALL_REQUIRES = [
    'PySide6>=6.4.3',
    'PyOpenGL>=3.1.6',
    'numpy>=1.24.2'
]

with codecs.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name=package_name,
    version='0.0.1',
    description='spartaproject',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lyoutakoduka',
    author='lyouta',
    author_email='lyouta@spartaproject.com',
    license='MIT',
    keywords='sparta spartaproject pyspartaproj',
    packages=[package_name],
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: GPU',
        'Environment :: X11 Applications :: Qt',
        'License :: OSI Approved :: MIT License'
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: C++',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: 3D Modeling'
    ]
)