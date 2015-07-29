from forms import CourseForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Course

# Create your views here.

def create_course(request):
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/courses')
    else:
        form = CourseForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_course.html', args)

def view_all_courses(request):
    
    if request.user.is_authenticated():
        template_name = "view_all_courses.html"
        courses = Course.objects.all()
        return render_to_response(template_name, {'courses':courses})
    else:
        return HttpResponseRedirect('/')


def view_course(request, pk):
    template_name = "view_course.html"
    course = Course.objects.get(pk=pk)
    return render_to_response(template_name, {'course':course})