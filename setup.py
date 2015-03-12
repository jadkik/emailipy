import sys

from setuptools import setup, find_packages


install_requires = [l.split('#')[0].strip()
                    for l in open('requirements.txt').readlines()
                    if not l.startswith('#') and not l.startswith('-e')]

setup(
    name='emailipy',
    packages = find_packages(),
    version='1.0',
    url='https://github.com/Parsely/emailipy',
    install_requires=install_requires
    )
