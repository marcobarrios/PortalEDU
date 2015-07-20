from forms import StaffAppointmentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import StaffAppointment

# Create your views here.

def create_staff_appointment(request):
    if request.POST:
        form = StaffAppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/staff-appointments')
    else:
        form = StaffAppointmentForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_appointment.html', args)

def view_all_staff_appointments(request):
    template_name = "view_all_staff_appointments.html"
    staffappointments = StaffAppointment.objects.all()
    return render_to_response(template_name, {'staffappointments':staffappointments})

def view_staff_appointment(request, pk):
    template_name = "view_staff_appointment.html"
    staffappointment = StaffAppointment.objects.get(pk=pk)
    return render_to_response(template_name, {'staffappointment':staffappointment})