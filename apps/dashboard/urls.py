from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.dashboard.views',
	url(r'^perfil/editar','editar_perfil',name='editar_perfil'),
	url(r'^crear/unico','new_user_view',name='new_user_unic'),
)