import os
from datetime import timedelta
from time import time
from threading import Lock
from django.conf import settings
from openid_connect import connect, connect_url

server_cache = None
server_cache_lock = Lock()
server_cache_expires = None

def get_server():
	global server_cache, server_cache_expires, server_cache_lock

	try:
		SERVER_CACHE_LOCK = settings.AUTH_SERVER_CACHE_LOCK
	except AttributeError:
		SERVER_CACHE_LOCK = True

	with server_cache_lock:
		now = time()

		if(SERVER_CACHE_LOCK):
			if not server_cache_expires or server_cache_expires <= now:
				AUTH_URL = os.environ.get("AUTH_URL")
				if AUTH_URL:
					server_cache = connect_url(AUTH_URL)
				else:
					server_cache = connect(settings.AUTH_SERVER, settings.AUTH_CLIENT_ID, settings.AUTH_CLIENT_SECRET, getattr(settings, 'AUTH_PROTOCOL', None))
				server_cache_expires = now + timedelta(hours=1).total_seconds()
		else:
			AUTH_URL = os.environ.get("AUTH_URL")
			if AUTH_URL:
				server_cache = connect_url(AUTH_URL)
			else:
				server_cache = connect(settings.AUTH_SERVER, settings.AUTH_CLIENT_ID, settings.AUTH_CLIENT_SECRET, getattr(settings, 'AUTH_PROTOCOL', None))

		return server_cache
