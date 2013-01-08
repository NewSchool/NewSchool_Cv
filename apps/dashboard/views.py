from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import PerfilForm, UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

@login_required
def editar_perfil(request):

    if request.method == 'POST':
        # formulario enviado
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, instance=request.user.perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            # formulario validado correctamente
            user_form.save()
            perfil_form.save()
            return HttpResponseRedirect('/data/')

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)

    return render_to_response('dashboard/perfil.jade', { 'user_form': user_form,  'perfil_form': perfil_form }, context_instance=RequestContext(request))


@login_required
def new_user_view(request):
    if request.method == 'POST':
        formulario  =   UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/data/')
    else:
        formulario  =   UserCreationForm(request.POST)
    return render_to_response('dashboard/new_user.jade',{'form':formulario} , context_instance=RequestContext(request))
