#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='kachapi',
    version='0.1.0',
    description='Generic OCR for Indian Languages',
    long_description=readme + '\n\n' + history,
    author='Arjun',
    author_email='arjun.kashyap@sriangadigital.com',
    url='https://github.com/arjunkashyap/kachapi',
    packages=[
        'kachapi',
    ],
    package_dir={'kachapi':
                 'kachapi'},
    include_package_data=True,
    install_requires=requirements,
    license="AGPL",
    zip_safe=False,
    keywords='kachapi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: AGPL License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
