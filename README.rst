Django-Auth-OIDC - OpenID Connect authentication support for Django
===================================================================
.. image:: https://badge.fury.io/py/django-auth-oidc.svg
	:target: https://badge.fury.io/py/django-auth-oidc

This is a Django login view that authenticates against an OpenID Connect
Authentication Server.

Use it if you own a single Authentication Server that you want to share
between multiple apps.

What is OpenID Connect?
-----------------------

It's a OAuth2-based standard for authentication in applications.

It can be used for social logins (but django-extauth_ is much better
for this case), and for setting up Single Sign-On into multiple services
hosted by the same company. In the last case, it somewhat supersedes LDAP,
as with OIDC people are entering their credentials only into the views
served by the Authentication Server, and not into all the company's
applications.

Requirements
------------

- Python 2.7 / 3.5+
- Django 1.10+
- openid-connect_

Installation
------------

.. code:: python

	pip install django-auth-oidc

settings.py
~~~~~~~~~~~

.. code:: python

	INSTALLED_APPS += ['django_auth_oidc']

urls.py
~~~~~~~

.. code:: python

	urlpatterns += [
		url(r'^accounts/login/', include('django_auth_oidc.urls')),
	]

Configuration
-------------

Authorization Server
~~~~~~~~~~~~~~~~~~~~

App's redirect URI: http(s)://app-domain/accounts/login/callback

Your application
~~~~~~~~~~~~~~~~

You may specify following settings in the Django settings file:

* AUTH_SERVER - OpenID Connect Authorization Server URL.
* AUTH_CLIENT_ID - Client ID received from the Authorization Server
* AUTH_CLIENT_SECRET - Client secret received from the Authorization Server
* AUTH_PROTOCOL (optional) - Legacy protocol supported by openid-connect_ library, for example github or gitlab. See openid-connect_'s documentation for full list of supported protocols.

Or, alternatively, you may set the AUTH_URL environment variable:

.. code:: bash

	AUTH_URL=(protocol+)http(s)://client_id:client_secret@server/

(Note: ":", "@", "/" and "%" inside client_id and client_secret must be urlquoted.)

.. _openid-connect: https://gitlab.com/aiakos/python-openid-connect
.. _django-extauth: https://github.com/aiakos/django-extauth
