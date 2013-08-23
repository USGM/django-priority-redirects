import os

from setuptools import setup, find_packages

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = 'django-priority-redirects',
	version = '0.2',
	url = 'https://github.com/USGM/django-priority-redirects',
	license = 'BSD License',
	description = "Tweak on the standard redirect app. Doesn't wait for a 404.",
	
	author = 'US Global Mail',
	author_email = 'it@usglobalmail.com',
	
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	
	install_requires = [
		'setuptools',
		'django',
  ],
	
	classifiers = [
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP',
	],
)
