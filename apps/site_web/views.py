from django.shortcuts import render_to_response
from django.template import RequestContext


def index_view(request):
	return render_to_response('site_web/index.jade',context_instance=RequestContext(request))
def login_view(request):
	return render_to_response('site_web/login.jade',context_instance=RequestContext(request))