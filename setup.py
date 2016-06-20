#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import os

setup(
    name="django-versionfield3",
    version="0.1.2",
    url="https://github.com/Crystalnix/django-versionfield3",
    license="BSD",
    description="A DB Independent Custom Django Field for storing Version numbers for fast indexing",
    author="Egor Yurtaev",
    author_email="yurtaev.egor+versionfield@gmail.com",
    packages=["versionfield"],
    include_package_data=True,
    install_requires=[
        "future>=0.14.3",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
    ]
)
