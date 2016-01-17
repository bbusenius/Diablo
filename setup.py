# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='diablo_python',
    description='Simple libraries and repurposable code ' + \
                'for inclusion in projects and general use.',
    version='0.0.1',
    author='Brad Busenius',
    packages = find_packages(),
    #py_modules=[
    #    'convert_php', 
    #    'file_parsing',
    #    'simple_math', 
    #], 
    url='https://github.com/bbusenius/Diablo-Python',
    license='BSD licence',
    install_requires=[
        'phpserialize',
    ],
    test_suite='tests',
    zip_safe=False
)
