# -*- coding: utf-8 -*-

# File copeid from https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='HashtagCreator',
    version='0.1.0',
    description='Simple Python script that takes text and creates hashtags for it',
    long_description=readme,
    author='Kevin Kanarbik',
    author_email='kevin.kanarbik@gmail.com',
    url='https://github.com/Kennu76/HashtagCreator',
    license=license,
    packages=find_packages()
)

