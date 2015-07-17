from django.contrib.auth.forms import UserCreationForm
from forms import InchargeForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .models import Incharge

# Create your views here.

def create_incharge(request):
    if request.method == 'POST':
        form_new_incharge = InchargeForm(request.POST)
        form_new_user = UserCreationForm(request.POST)
        if form_new_user.is_valid and form_new_incharge.is_valid:
            form_new_user.save()
            form_new_incharge.save()
            return HttpResponseRedirect('/incharges')
    else:
        form_new_incharge = InchargeForm()
        form_new_user = UserCreationForm()

    return render_to_response('new_incharge.html', { 'form_new_user':form_new_user, 'form_new_incharge':form_new_incharge}, context_instance = RequestContext(request))

def view_all_incharges(request):
    template_name = "view_all_incharges.html"
    incharges = Incharge.objects.all()
    return render_to_response(template_name, {'incharges':incharges})

def view_incharge(request, pk):
    template_name = "view_incharge.html"
    incharge = Incharge.objects.get(pk=pk)
    return render_to_response(template_name, {'incharge':incharge})
