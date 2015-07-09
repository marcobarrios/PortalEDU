from forms import ExtraCurricularActivityForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_extra_curricular_activity(request):
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
    if request.POST:
        form = ExtraCurricularActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ExtraCurricularActivityForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_extra_curricular_activity.html', args)