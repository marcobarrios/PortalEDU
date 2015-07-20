from forms import LevelForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Level

# Create your views here.

def create_level(request):
    if request.POST:
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/levels')
    else:
        form = LevelForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_level.html', args)

def view_all_levels(request):
    template_name = "view_all_levels.html"
    levels = Level.objects.all()
    return render_to_response(template_name, {'levels':levels})

def view_level(request, pk):
    template_name = "view_level.html"
    level = Level.objects.get(pk=pk)
    return render_to_response(template_name, {'level':level})