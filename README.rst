Django-Auth-OIDC - OpenID Connect authentication support for Django
=========================================================================
.. image:: https://badge.fury.io/py/django-auth-oidc.svg
    :target: https://badge.fury.io/py/django-auth-oidc

This is a Django login view that authenticates against an OpenID Connect
Authentication Server.

Use it if you own a single Authentication Server that you want to share
between multiple apps.

What is OpenID Connect?
-----------------------

It's a OAuth2-based standard for authentication in applications.

It can be used for social logins (but python-social-auth_ is much better
for this case), and for setting up Single Sign-On into multiple services
hosted by the same company. In the last case, it somewhat supersedes LDAP,
as with OIDC people are entering their credentials only into the views
served by the Authentication Server, and not into all the company's
applications.

Requirements
------------

- Python 3.6+. **Python 2 is not supported, and won’t ever get supported.**
- Django 1.10+
- python-jose_

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

App's environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OIDC_SERVER - OpenID Connect Authorization Server URL.
* OIDC_CLIENT_ID - Client ID received from the Authorization Server
* OIDC_CLIENT_SECRET - Client secret received from the Authorization Server

.. _python-jose: https://github.com/mpdavis/python-jose
.. _python-social-auth: https://github.com/omab/python-social-auth
