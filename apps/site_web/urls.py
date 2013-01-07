from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.site_web.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^login','login_view',name='vista_login'),
)