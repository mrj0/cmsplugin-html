#!/usr/bin/env python
import os
from setuptools import setup, find_packages

import cmsplugin_html

setup(
    name='cmsplugin-html',
    version= '0.1',
    description='A very simple plugin for django-cms 2 for plain html',
    long_description=open('README.md').read(),
    #author='',
    #author_email='X',
    maintainer='Mike Johnson',
    maintainer_email='mike@publicstatic.net',
    url='https://github.com/mrj0/cmsplugin-html',
    license='MIT',
    packages=find_packages(),
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
