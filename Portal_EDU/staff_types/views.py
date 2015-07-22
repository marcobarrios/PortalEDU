from forms import StaffType
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import StaffType

# Create your views here.

def create_staff_type(request):
    if request.POST:
        form = StaffType(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/staff-types')
    else:
        form = StaffType()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_staff_type.html', args)

def view_all_staff_types(request):
    template_name = "view_all_staff_types.html"
    stafftypes = StaffType.objects.all()
    return render_to_response(template_name, {'stafftypes':stafftypes})

def view_staff_type(request, pk):
    template_name = "view_staff_type.html"
    stafftype = StaffType.objects.get(pk=pk)
    return render_to_response(template_name, {'stafftype':stafftype})