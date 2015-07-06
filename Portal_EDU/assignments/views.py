from forms import AssignmentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_assignment(request):
    if request.POST:
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = AssignmentForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_assignment.html', args)