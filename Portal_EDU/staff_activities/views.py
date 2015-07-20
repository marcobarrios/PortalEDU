from forms import StaffActivityForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import StaffActivity

# Create your views here.

def create_staff_activity(request):
    if request.POST:
        form = StaffActivityForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/staff-activities')
    else:
        form = StaffActivityForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_activity.html', args)

def view_all_staff_activities(request):
    template_name = "view_all_staff_activities.html"
    staffactivities = StaffActivity.objects.all()
    return render_to_response(template_name, {'staffactivities':staffactivities})

def view_staff_activity(request, pk):
    template_name = "view_staff_activity.html"
    staffactivity = StaffActivity.objects.get(pk=pk)
    return render_to_response(template_name, {'staffactivity':staffactivity})