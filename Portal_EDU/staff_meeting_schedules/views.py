from forms import StaffMeetingScheduleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import StaffMeetingSchedule

# Create your views here.

def create_staff_meeting_schedule(request):
    if request.POST:
        form = StaffMeetingScheduleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/staff-meeting-schedules')
    else:
        form = StaffMeetingScheduleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_meeting_schedule.html', args)

def view_all_staff_meeting_schedules(request):
    template_name = "view_all_staff_meeting_schedules.html"
    staffmeetingschedules = StaffMeetingSchedule.objects.all()
    return render_to_response(template_name, {'staffmeetingschedules':staffmeetingschedules})

def view_staff_meeting_schedule(request, pk):
    template_name = "view_staff_meeting_schedule.html"
    staffmeetingschedule = StaffMeetingSchedule.objects.get(pk=pk)
    return render_to_response(template_name, {'staffmeetingschedule':staffmeetingschedule})