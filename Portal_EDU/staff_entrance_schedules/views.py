from forms import StaffEntranceScheduleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import StaffEntranceSchedule

# Create your views here.

def create_staff_entrance_schedule(request):
    if request.POST:
        form = StaffEntranceScheduleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/staff-entrance-schedules')
    else:
        form = StaffEntranceScheduleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_entrance_schedule.html', args)

def view_all_staff_entrance_schedules(request):
    template_name = "view_all_staff_entrance_schedules.html"
    staffentranceschedules = StaffEntranceSchedule.objects.all()
    return render_to_response(template_name, {'staffentranceschedules':staffentranceschedules})

def view_staff_entrance_schedule(request, pk):
    template_name = "view_staff_entrance_schedule.html"
    staffentranceschedule = StaffEntranceSchedule.objects.get(pk=pk)
    return render_to_response(template_name, {'staffentranceschedule':staffentranceschedule})