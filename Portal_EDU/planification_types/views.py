from forms import PlanificationTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_planification_type(request):
    if request.POST:
        form = PlanificationTypeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = PlanificationTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_planification_type.html', args)