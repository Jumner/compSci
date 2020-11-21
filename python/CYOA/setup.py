import os
from setuptools import setup, Extension
from glob import glob

lib = ('cppGood', dict(
	sources=glob('src/*.cpp'),
	include_dirs=['include', '/usr/include/python3.9'],
	language='c++'
))

module = Extension(
	'cppGood',
	sources=glob('src/*.cpp'),
	include_dirs=['include', '/usr/include/python3.9'],
	language='c++'
)

setup(
	name='cppGood',
	version='0.0.0',
	url="https://github.com/Jumner/compSci/tree/main/python/CYOA",
	description="A library for choose your own adventure games",
	libraries = [lib],
	ext_modules = [module]
)