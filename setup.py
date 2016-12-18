# coding: utf-8
from __future__ import unicode_literals
from distutils.core import setup

setup(
    name='flynsarmy-paginator',
    packages=['flynsarmy_paginator'],
    version='0.0.1',
    author='Flynsarmy',
    author_email='flynsarmy@gmail.com',
    maintainer='Flynsarmy',
    maintainer_email='flynsarmy@gmail.com',
    url='https://github.com/Flynsarmy/flynsarmy-paginator',
    license='README',
    description='Adds floating (ranged) pagination support to Django\'s '
                'paginator class',
    long_description='Adds floating (ranged) pagination support to Django\'s '
                     'paginator class. See https://www.flynsarmy.com/2011/06/'
                     'floating-page-numbers-in-django/',
    install_requires=[
        'Django>=1.8.15',
    ],
    classifiers=[
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Other/Nonlisted Topic',
    ],
)
