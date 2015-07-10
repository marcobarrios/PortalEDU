from forms import MedicalBackGroundForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_medical_background(request):
    if request.POST:
        form = MedicalBackGroundForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MedicalBackGroundForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_medical_background.html', args)