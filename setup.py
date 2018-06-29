#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:15:01 2018

@author: shubham
"""

from setuptools import setup

setup(name='themodulex',
      version='0.1',
      description='Common utility files for JSON manipulation.',
      url='http://github.com/shubhamcxz',
      author='Shubham CXZ',
      author_email='shubhamcxz@gmail.com',
      license='MIT',
      packages=['themodulex'],
      username="shubhamcxz",
      install_requires=['numpy',],
      # dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'] # when dependency is not on pypi
      zip_safe=False)
