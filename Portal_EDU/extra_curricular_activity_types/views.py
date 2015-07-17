from forms import ExtraCurricularActivityTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import ExtraCurricularActivityType

# Create your views here.

def create_extracurricularactivitytype(request):
    if request.POST:
        form = ExtraCurricularActivityTypeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/extra-curricular-activity-types')
    else:
        form = ExtraCurricularActivityTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_extracurricularactivitytype.html', args)

def view_all_extra_curricular_activity_types(request):
    template_name = "view_all_extra_curricular_activity_types.html"
    extracurricularactivitytypes = ExtraCurricularActivityType.objects.all()
    return render_to_response(template_name, {'extracurricularactivitytypes':extracurricularactivitytypes})

def view_extra_curricular_activity_type(request, pk):
    template_name = "view_extra_curricular_activity_type.html"
    extracurricularactivitytype = ExtraCurricularActivityType.objects.get(pk=pk)
    return render_to_response(template_name, {'extracurricularactivitytype':extracurricularactivitytype})