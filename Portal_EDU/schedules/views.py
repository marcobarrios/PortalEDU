from forms import ScheduleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Schedule

# Create your views here.

def create_schedule(request):
    if request.POST:
        form = SheduleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/schedules')
    else:
        form = ScheduleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_schedule.html', args)

def view_all_schedules(request):
    template_name = "view_all_schedules.html"
    schedules = Schedule.objects.all()
    return render_to_response(template_name, {'schedules':schedules})

def view_schedule(request, pk):
    template_name = "view_schedule.html"
    schedule = Schedule.objects.get(pk=pk)
    return render_to_response(template_name, {'schedule':schedule})