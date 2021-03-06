from distutils.core import setup

from setuptools import find_packages

setup(
    name='python-restcountries',
    version='0.1a3',
    author='Robert Stein',
    author_email='robert@blueshoe.de',
    url='https://github.com/SteinRobert/python-restcountries',
    download_url='https://github.com/SteinRobert/python-restcountries/tarball/0.1a3',
    packages=find_packages(),
    dependencies=['future', 'requests'],
    description='Python API Wrapper for restcountries.eu',
    license='Unlicense',
    keywords=['api', 'wrapper', 'country', 'countries'],
    install_requires=[
        'requests',
        'future'
    ],
    long_description=open('README.rst').read()
)