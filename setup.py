#!/usr/bin/env python

# setup from https://bitbucket.org/xenofox/cmsplugin-plaintext/

from setuptools import setup, find_packages
PACKAGE_NAME = 'cmsplugin_html'
PACKAGE_DIR = PACKAGE_NAME

import os, sys

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

def fullsplit(path, result=None):
    """
    Split a pathname into compontents (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell disutils to put the data_files in platofmr-specific installation
# locations.
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distuils doesn't have
# and easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk(PACKAGE_DIR):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append(
                [dirpath, [os.path.join(dirpath, f) for f in filenames]]
                )
# Small hack for working with bdist_wininst
# See http://mail.python.org/pipermail/distutils-sig/2004-August/004134.html
if len(sys.argv) > 1 and sys.argv[1] == 'bdist_wininst':
    for file_info in data_files:
        file_info[0] = '\\PURELIB\\%s' % file_info[0]

setup(
    name='cmsplugin-html',
    version= '0.1',
    description='A very simple plugin for django-cms 2 for plain html',
    long_description=open('README.md').read(),
    #author='',
    #author_email='X',
    maintainer='mrj0',
    maintainer_email='mike@publicstatic.net',
    url='https://github.com/mrj0/cmsplugin-html',
    license='MIT',
    packages=packages,
    data_files=data_files,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
