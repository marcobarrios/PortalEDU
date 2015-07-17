from forms import ExtraCurricularActivityForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import ExtraCurricularActivity

# Create your views here.

def create_extra_curricular_activity(request):
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
    if request.POST:
        form = ExtraCurricularActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/extra-curricular-activities')
    else:
        form = ExtraCurricularActivityForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_extra_curricular_activity.html', args)

def view_all_extra_curricular_activities(request):
    template_name = "view_all_extra_curricular_activities.html"
    extracurricularactivities = ExtraCurricularActivity.objects.all()
    return render_to_response(template_name, {'extracurricularactivities':extracurricularactivities})

def view_extra_curricular_activity(request, pk):
    template_name = "view_extra_curricular_activity.html"
    extracurricularactivity = ExtraCurricularActivity.objects.get(pk=pk)
    return render_to_response(template_name, {'extracurricularactivity':extracurricularactivity})