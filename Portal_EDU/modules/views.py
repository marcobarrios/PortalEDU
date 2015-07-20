from forms import ModuleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Module

# Create your views here.

def create_module(request):
    if request.POST:
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/modules')
    else:
        form = ModuleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_module.html', args)

def view_all_modules(request):
    template_name = "view_all_modules.html"
    modules = Module.objects.all()
    return render_to_response(template_name, {'modules':modules})

def view_module(request, pk):
    template_name = "view_module.html"
    module = Module.objects.get(pk=pk)
    return render_to_response(template_name, {'module':module})