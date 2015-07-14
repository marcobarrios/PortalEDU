from forms import StaffActivityForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_staff_activity(request):
    if request.POST:
        form = StaffActivityForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = StaffActivityForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_activity.html', args)