from forms import AssignmentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Assignment

# Create your views here.

def create_assignment(request):
    if request.POST:
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/assignments')
    else:
        form = AssignmentForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_assignment.html', args)

def view_all_assignments(request):
    template_name = "view_all_assignments.html"
    assignments = Assignment.objects.all()
    return render_to_response(template_name, {'assignments':assignments})

def view_assignment(request, pk):
    template_name = "view_assignment.html"
    assignment = Assignment.objects.get(pk=pk)
    return render_to_response(template_name, {'assignment':assignment})