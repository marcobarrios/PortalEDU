from forms import MedicalBackGroundForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import MedicalBackGround

# Create your views here.

def create_medical_background(request):
    if request.POST:
        form = MedicalBackGroundForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medical-backgrounds')
    else:
        form = MedicalBackGroundForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_medical_background.html', args)

def view_all_medical_backgrounds(request):
    template_name = "view_all_medical_backgrounds.html"
    medicalbackgrounds = MedicalBackGround.objects.all()
    return render_to_response(template_name, {'medicalbackgrounds':medicalbackgrounds})

def view_medical_background(request, pk):
    template_name = "view_medical_background.html"
    medicalbackground = MedicalBackground.objects.get(pk=pk)
    return render_to_response(template_name, {'medicalbackground':medicalbackground})