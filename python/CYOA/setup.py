import os
from setuptools import setup, Extension

module = Extension('cppGood', sources=['src/main.cpp'], language='c++')

setup(name='cppGood', ext_modules = [module])