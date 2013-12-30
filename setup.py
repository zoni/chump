# -*- coding: utf-8 -*-

import sys
import os.path


try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

install_requires = []
for line in open('requirements.txt', 'rU').readlines():
	if line and line not in '\n' and not line.startswith(('#', '-')):
		install_requires.append(line.replace('\n', ''))

kwargs = {}
if sys.version_info >= (3,):
	kwargs['use_2to3'] = True

setup(
	name="chump",
	version=open(os.path.join(os.path.dirname(__file__), "chump", "version")).read().strip(),
	description="A fully featured API wrapper for Pushover.",
	long_description="\n\n".join([open('README.rst', 'rU').read(), open('HISTORY.rst', 'rU').read()]),
	author='Karan Lyons',
	author_email='karan@karanlyons.com',
	url='https://github.com/karanlyons/chump',
	license=open('LICENSE', 'rU').read(),
	packages=['chump'],
	package_dir={'chump': 'chump'},
	package_data={'': ['README.rst', 'HISTORY.rst', 'LICENSE']},
	include_package_data=True,
	install_requires=install_requires,
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
