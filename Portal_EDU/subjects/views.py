from forms import SubjectForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Subject

# Create your views here.

def create_subject(request):
    if request.POST:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/subjects')
    else:
        form = SubjectForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_subject.html', args)

def view_all_subjects(request):
    template_name = "view_all_subjects.html"
    subjects = Subject.objects.all()
    return render_to_response(template_name, {'subjects':subjects})

def view_subject(request, pk):
    template_name = "view_subject.html"
    subject = Subject.objects.get(pk=pk)
    return render_to_response(template_name, {'subject':subject})