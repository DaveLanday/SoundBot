#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#setup.py
#Dave Landay
#LAST UPDATED: 04-09-2020

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(version='1.0.0',
      name='soundBot',
      description='A Discord bot that integrates soundboards into chat.',
      author='Dave Landay, Caio Ingber',
      author_email='',
      packages=find_packages(),
      install_requires=required,
      test_suite='tests')
