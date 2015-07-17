from forms import EntranceScheduleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import EntranceSchedule

# Create your views here.

def create_entrance_schedule(request):
    if request.POST:
        form = EntranceScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/entrance-schedules')
    else:
        form = EntranceScheduleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_entrance_schedule.html', args)

def view_all_entrance_schedules(request):
    template_name = "view_all_entrance_schedules.html"
    entranceschedules = EntranceSchedule.objects.all()
    return render_to_response(template_name, {'entranceschedules':entranceschedules})

def view_entrance_schedule(request, pk):
    template_name = "view_entrance_schedule.html"
    entranceschedule = EntranceSchedule.objects.get(pk=pk)
    return render_to_response(template_name, {'entranceschedule':entranceschedule})