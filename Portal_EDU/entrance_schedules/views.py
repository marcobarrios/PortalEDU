from forms import EntranceScheduleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_entrance_schedule(request):
    if request.POST:
        form = EntranceScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EntranceScheduleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_entrance_schedule.html', args)