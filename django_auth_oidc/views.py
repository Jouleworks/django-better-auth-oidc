from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect, resolve_url
try:
	from django.urls import reverse
except ImportError:
	from django.core.urlresolvers import reverse # deprecated since Django 1.10
from django.utils.http import is_safe_url

from . import auth as _auth

try:
	LOGIN_REDIRECT_URL = settings.LOGIN_REDIRECT_URL
except AttributeError:
	LOGIN_REDIRECT_URL = '/'

try:
	LOGOUT_REDIRECT_URL = settings.LOGOUT_REDIRECT_URL
except AttributeError:
	LOGOUT_REDIRECT_URL = '/'

try:
	AUTH_SCOPE = settings.AUTH_SCOPE
except AttributeError:
	AUTH_SCOPE = ('openid',)


def login(request):
	return_path = request.GET.get(auth.REDIRECT_FIELD_NAME, "")

	return redirect(_auth.server.authorize(
		redirect_uri = request.build_absolute_uri(reverse("django_auth_oidc:login-done")),
		state = return_path,
		scope = AUTH_SCOPE,
	))


def callback(request):
	return_path = request.GET.get("state")

	res = _auth.server.request_token(
		redirect_uri = request.build_absolute_uri(reverse("django_auth_oidc:login-done")),
		code = request.GET["code"],
	)

	User = auth.get_user_model()
	user, created = User.objects.get_or_create(username=res.id["sub"])
	auth.login(request, user)
	request.session['openid_token'] = res.id_token
	request.session['openid'] = res.id

	url_is_safe = is_safe_url(
		url = return_path,
		host = request.get_host(),
		#allowed_hosts = set(request.get_host()),
		#require_https = request.is_secure(),
	)
	if not url_is_safe:
		return redirect(resolve_url(LOGIN_REDIRECT_URL))
	return redirect(return_path)


def logout(request):
	id_token = request.session.get('openid_token', '')
	auth.logout(request)

	if _auth.server.end_session_endpoint:
		return redirect(_auth.server.end_session(
			post_logout_redirect_uri = request.build_absolute_uri(LOGOUT_REDIRECT_URL),
			state = '',
			id_token_hint = id_token,
		))
	else:
		return redirect(request.build_absolute_uri(LOGOUT_REDIRECT_URL))
