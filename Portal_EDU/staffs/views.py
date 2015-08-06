from django.contrib.auth.forms import UserCreationForm
from forms import StaffForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.

def create_staff(request):
    if request.method == 'POST':
        form_new_staff = StaffForm(request.POST)
        form_new_user = UserCreationForm(request.POST)
        if form_new_user.is_valid and form_new_staff.is_valid:
            form_new_user.save()
            form_new_staff.save()
            return HttpResponseRedirect('/')
    else:
        form_new_staff = StaffForm()
        form_new_user = UserCreationForm()

    return render_to_response('new_staff.html', { 'form_new_user':form_new_user, 'form_new_staff':form_new_staff}, context_instance = RequestContext(request))

def portal_teacher(request):
    return render_to_response('principal-maestros.html', context_instance = RequestContext(request))

def portal_administrative(request):
    return render_to_response('principal-administrativo.html', context_instance = RequestContext(request))
