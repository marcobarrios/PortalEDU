from forms import StaffForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_staff(request):
    if request.POST:
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = StaffForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff.html', args)