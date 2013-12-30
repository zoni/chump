# -*- coding: utf-8 -*-

import sys

import chump

from pip.req import parse_requirements


try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

kwargs = {}
if sys.version_info >= (3,):
	kwargs['use_2to3'] = True

setup(
	name="chump",
	version=chump.__version__,
	description="A fully featured API wrapper for Pushover.",
	long_description="\n\n".join([open('README.rst', 'rU').read(), open('HISTORY.rst', 'rU').read()]),
	author=chump.__author__,
	author_email=chump.__contact__,
	url=chump.__homepage__,
	license=open('LICENSE', 'rU').read(),
	packages=['chump'],
	package_dir={'chump': 'chump'},
	package_data={'': ['README.rst', 'HISTORY.rst', 'LICENSE']},
	include_package_data=True,
	install_requires=[str(r.req) for r in parse_requirements('requirements.txt')],
	zip_safe=False,
	classifiers=(
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
	),
	**kwargs
)
