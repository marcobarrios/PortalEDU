from forms import GradeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Grade

# Create your views here.

def create_grade(request):
    if request.POST:
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/grades')
    else:
        form = GradeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_grade.html', args)

def view_all_grades(request):
    template_name = "view_all_grades.html"
    grades = Grade.objects.all()
    return render_to_response(template_name, {'grades':grades})

def view_grade(request, pk):
    template_name = "view_grade.html"
    grade = Grade.objects.get(pk=pk)
    return render_to_response(template_name, {'grade':grade})