from forms import SchoolForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import School

# Create your views here.

def create_school(request):
    if request.POST:
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/schools')
    else:
        form = SchoolForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_school.html', args)

def view_all_schools(request):
    template_name = "view_all_schools.html"
    schools = School.objects.all()
    return render_to_response(template_name, {'schools':schools})

def view_school(request, pk):
    template_name = "view_school.html"
    school = School.objects.get(pk=pk)
    return render_to_response(template_name, {'school':school})