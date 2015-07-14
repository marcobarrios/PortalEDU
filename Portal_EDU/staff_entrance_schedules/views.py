from forms import StaffEntranceScheduleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_staff_entrance_schedule(request):
    if request.POST:
        form = StaffEntranceScheduleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = StaffEntranceScheduleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_entrance_schedule.html', args)