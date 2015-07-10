from forms import InchargeTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_incharge_type(request):
    if request.POST:
        form = InchargeTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = InchargeTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_incharge_type.html', args)