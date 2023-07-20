Django-Better-Auth-OIDC - OpenID Connect authentication support for Django
==========================================================================

This is a Django login view that authenticates against an OpenID Connect
Authentication Server.

Use it if you own a single Authentication Server that you want to share
between multiple apps.

Huh?
----

This is a fork of the abandoned django-auth-oidc_. Original code by the Aiakos_ team.


What is OpenID Connect?
-----------------------

It's a OAuth2-based standard for authentication in applications.

It can be used for social logins, and for setting up Single Sign-On into multiple services
hosted by the same company. In the last case, it somewhat supersedes LDAP,
as with OIDC people are entering their credentials only into the views
served by the Authentication Server, and not into all the company's
applications.

Requirements
------------

- Python 3.5+
- Django 4.x+
- openid-connect_

Installation
------------

.. code:: python

	pip install django-better-auth-oidc

settings.py
~~~~~~~~~~~

.. code:: python

	INSTALLED_APPS += ['django_better_auth_oidc']

urls.py
~~~~~~~

.. code:: python

	urlpatterns += [
		path('auth/', include('django_better_auth_oidc.urls')),
	]

Configuration
-------------

Server Cache Lock
~~~~~~~~~~~~~~~~~
By default, DBAO will only fetch the server info based on a cache lock timer. To disable this feature, use the setting AUTH_SERVER_CACHE_LOCK and set to false.

Authorization Server
~~~~~~~~~~~~~~~~~~~~

App's redirect URI: http(s)://app-domain/auth/done
App's post-logout redirect URI: http(s)://app-domain/*LOGOUT_REDIRECT_URL* (or / if not set)

Authorization Server details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may specify following settings in the Django settings file:

* AUTH_SERVER - OpenID Connect Authorization Server URL.
* AUTH_CLIENT_ID - Client ID received from the Authorization Server
* AUTH_CLIENT_SECRET - Client secret received from the Authorization Server
* AUTH_PROTOCOL (optional) - Legacy protocol supported by openid-connect_ library, for example github or gitlab. See openid-connect_'s documentation for full list of supported protocols.

Or, alternatively, you may set the AUTH_URL environment variable:

.. code:: bash

	AUTH_URL=(protocol+)http(s)://client_id:client_secret@server/

(Note: ":", "@", "/" and "%" inside client_id and client_secret must be urlquoted.)

Behavior
~~~~~~~~

* AUTH_SCOPE (default: ['openid']) - list of scopes to request from the auth server
* AUTH_GET_USER_FUNCTION (default: 'django_auth_oidc:get_user_by_username') - name of a function that takes the user info dict, and returns an user object representing that user; note that it should set the user.backend attribute.

.. _openid-connect: https://gitlab.com/aiakos/python-openid-connect
.. _Aiakos: https://gitlab.com/aiakos/aiakos
.. _django-auth-oidc: https://pypi.org/project/django-auth-oidc/
