from forms import BloodTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import BloodType

# Create your views here.

def create_blood_type(request):
    if request.POST:
        form = BloodTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blood-types')
    else:
        form = BloodTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_blood_type.html', args)

def view_all_blood_types(request):
    template_name = "view_all_blood_types.html"
    bloodtypes = BloodType.objects.all()
    return render_to_response(template_name, {'bloodtypes':bloodtypes})

def view_blood_type(request, pk):
    template_name = "view_blood_type.html"
    bloodtype = BloodType.objects.get(pk=pk)
    return render_to_response(template_name, {'bloodtype':bloodtype})