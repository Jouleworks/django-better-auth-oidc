#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
	readme = f.read()

setup(
	name = "django-better-auth-oidc",
	version = "0.1.1",
	description = "Better OpenID Connect authentication support for Django",
	long_description = readme,
	author = "Jouleworks Development Contributors",
	author_email = "hello@jouleworksdev.com",
	url = "https://github.com/jouleworks/django-better-auth-oidc",
	keywords = "django auth oauth openid oidc social ldap",

	install_requires = ['django>=4.0.0', 'openid_connect'],

	packages = ["django_better_auth_oidc"],
	zip_safe = True,

	license = "MIT",
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Framework :: Django',
		'Framework :: Django :: 4.0',
		'Framework :: Django :: 4.1',
		'Framework :: Django :: 4.2',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: MIT License',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
	]
)
