import os

from django.conf import settings

from openid_connect import connect, connect_url

AUTH_URL = os.environ.get("AUTH_URL")
if AUTH_URL:
	server = connect_url(AUTH_URL)
else:
	server = connect(settings.AUTH_SERVER, settings.AUTH_CLIENT_ID, settings.AUTH_CLIENT_SECRET, getattr(settings, 'AUTH_PROTOCOL', None))
