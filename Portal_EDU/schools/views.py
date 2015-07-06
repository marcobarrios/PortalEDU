from forms import SchoolForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_school(request):
    if request.POST:
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = SchoolForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_school.html', args)