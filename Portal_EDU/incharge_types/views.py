from forms import InchargeTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import InchargeType

# Create your views here.

def create_incharge_type(request):
    if request.POST:
        form = InchargeTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/incharge-types')
    else:
        form = InchargeTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_incharge_type.html', args)

def view_all_incharge_types(request):
    template_name = "view_all_incharge_types.html"
    inchargetypes = InchargeType.objects.all()
    return render_to_response(template_name, {'inchargetypes':inchargetypes})

def view_incharge_type(request, pk):
    template_name = "view_incharge_type.html"
    inchargetype = InchargeType.objects.get(pk=pk)
    return render_to_response(template_name, {'inchargetype':inchargetype})