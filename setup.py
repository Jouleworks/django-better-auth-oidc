#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
	readme = f.read()

setup(
	name = "django-auth-oidc",
	version = "0.5.0",
	description = "OpenID Connect authentication support for Django",
	long_description = readme,
	author = "Aiakos Contributors",
	author_email = "aiakos@aiakosauth.com",
	url = "https://gitlab.com/aiakos/django-auth-oidc",
	keywords = "django auth oauth openid oidc social ldap",

	install_requires = ['django>=2.0.0', 'openid_connect'],

	packages = ["django_auth_oidc"],
	zip_safe = True,

	license = "MIT",
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Framework :: Django',
		'Framework :: Django :: 2.0',
		'Framework :: Django :: 2.1',
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
