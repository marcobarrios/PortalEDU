from forms import InchargeAppointmentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_incharge_appointment(request):
    if request.POST:
        form = InchargeAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = InchargeAppointmentForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('incharge_appointment.html', args)