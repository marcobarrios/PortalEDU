from forms import InchargeAppointmentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import InchargeAppointment

# Create your views here.

def create_incharge_appointment(request):
    if request.POST:
        form = InchargeAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/incharge-appointments')
    else:
        form = InchargeAppointmentForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('incharge_appointment.html', args)

def view_all_incharge_appointments(request):
    template_name = "view_all_incharge_appointments.html"
    inchargeappointments = InchargeAppointment.objects.all()
    return render_to_response(template_name, {'inchargeappointments':inchargeappointments})

def view_incharge_appointment(request, pk):
    template_name = "view_incharge_appointment.html"
    inchargeappointment = InchargeAppointment.objects.get(pk=pk)
    return render_to_response(template_name, {'inchargeappointment':inchargeappointment})