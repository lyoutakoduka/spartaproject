# -*- coding: utf-8 -*-

import setuptools
import codecs

package_name = 'pyspartaproj'
email = 'lyouta@spartaproject.com'
author_name = 'lyouta'
search_keywords = 'sparta spartaproject pyspartaproj'
package_version = '0.0.1'
package_description = 'spartaproject'
product_url = 'https://github.com/lyoutakoduka'
content_type = 'text/markdown'
license_type = 'MIT'

readme_path = 'README.md'

INSTALL_REQUIRES = [
    'PySide6>=6.4.3',
    'PyOpenGL>=3.1.6',
    'numpy>=1.24.2'
]

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
    'Topic :: Multimedia :: Graphics :: 3D Modeling'
]

with codecs.open(readme_path, encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name=package_name,
    version=package_version,
    description=package_description,
    long_description=long_description,
    long_description_content_type=content_type,
    url=product_url,
    author=author_name,
    author_email=email,
    license=license_type,
    keywords=search_keywords,
    packages=[package_name],
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS
)
