from forms import PlanificationTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import PlanificationType

# Create your views here.

def create_planification_type(request):
    if request.POST:
        form = PlanificationTypeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/planification-types')
    else:
        form = PlanificationTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_planification_type.html', args)

def view_all_planification_types(request):
    template_name = "view_all_planification_types.html"
    planificationtypes = PlanificationType.objects.all()
    return render_to_response(template_name, {'planificationtypes':planificationtypes})

def view_planification_type(request, pk):
    template_name = "view_planification_type.html"
    planificationtype = PlanificationType.objects.get(pk=pk)
    return render_to_response(template_name, {'planificationtype':planificationtype})