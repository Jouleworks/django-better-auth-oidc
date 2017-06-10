#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
	readme = f.read()

setup(
	name = "django-auth-oidc",
	version = "0.4.1",
	description = "OpenID Connect authentication support for Django",
	long_description = readme,
	author = "Aiakos Contributors",
	author_email = "aiakos@aiakosauth.com",
	url = "https://gitlab.com/aiakos/django-auth-oidc",
	keywords = "django auth oauth openid oidc social ldap",

	install_requires = ['django>=1.8.0', 'openid_connect'],

	packages = ["django_auth_oidc"],
	zip_safe = True,

	license = "MIT",
	classifiers = [
		'Development Status :: 4 - Beta',
		'Framework :: Django',
		'Framework :: Django :: 1.8',
		'Framework :: Django :: 1.9',
		'Framework :: Django :: 1.10',
		'Framework :: Django :: 1.11',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: MIT License',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
	]
)
