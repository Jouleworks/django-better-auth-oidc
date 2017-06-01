from django.conf.urls import url
from . import views

app_name = 'django_auth_oidc'
urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^done/$', views.callback, name='login-done'),
	url(r'^logout/$', views.logout, name='logout'),
]
