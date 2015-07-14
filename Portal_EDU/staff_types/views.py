from forms import StaffType
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_staff_type(request):
    if request.POST:
        form = StaffType(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = StaffType()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_type.html', args)