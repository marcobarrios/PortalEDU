from django.contrib.auth.forms import UserCreationForm
from forms import InchargeForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.

def create_incharge(request):
    if request.method == 'POST':
        form_new_incharge = InchargeForm(request.POST)
        form_new_user = UserCreationForm(request.POST)
        if form_new_user.is_valid and form_new_incharge.is_valid:
            form_new_user.save()
            form_new_incharge.save()
            return HttpResponseRedirect('/')
    else:
        form_new_incharge = InchargeForm()
        form_new_user = UserCreationForm()

    return render_to_response('new_incharge.html', { 'form_new_user':form_new_user, 'form_new_incharge':form_new_incharge}, context_instance = RequestContext(request))
