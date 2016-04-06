#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
	name='dosmav',
	version='0.0.1',
	description='Plugin to connect maven and dosocs for relationships',
	url='https://github.com/bwolatz/CSCI4900',
	author='Nikhit Adusumilli, Brain',
	license='MIT',
	
	keywords='spdx licenses maven dosocs2',
	packages=['src'],
	
	install_requires=['treelib'],	

	entry_points={'console_scripts':['dosmav=src.main:main']},
	zip_safe=False
)
