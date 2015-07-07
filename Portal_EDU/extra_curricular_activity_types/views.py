from forms import ExtraCurricularActivityTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_extracurricularactivitytype(request):
    if request.POST:
        form = ExtraCurricularActivityTypeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = ExtraCurricularActivityTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_extracurricularactivitytype.html', args)