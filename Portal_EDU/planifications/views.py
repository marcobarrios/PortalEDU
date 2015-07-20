from forms import PlanificationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Planification

# Create your views here.

def create_planification(request):
    if request.POST:
        form = PlanificationForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/planifications')
    else:
        form = PlanificationForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_planification.html', args)

def view_all_planifications(request):
    template_name = "view_all_planifications.html"
    planifications = Planification.objects.all()
    return render_to_response(template_name, {'planifications':planifications})

def view_planification(request, pk):
    template_name = "view_planification_type.html"
    planification = Planification.objects.get(pk=pk)
    return render_to_response(template_name, {'planification':planification})