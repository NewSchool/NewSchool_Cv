from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.database.views',
	url(r'^$','editar_perfil',name='editar_perfil'),
)