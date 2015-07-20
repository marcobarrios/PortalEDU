from forms import TaskForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Task

# Create your views here.

def create_task(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/tasks')
    else:
        form = TaskForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_task.html', args)

def view_all_tasks(request):
    template_name = "view_all_tasks.html"
    tasks = Task.objects.all()
    return render_to_response(template_name, {'tasks':tasks})

def view_task(request, pk):
    template_name = "view_task.html"
    task = Task.objects.get(pk=pk)
    return render_to_response(template_name, {'task':task})