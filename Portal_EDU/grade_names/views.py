from forms import GradeNameForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import GradeName

# Create your views here.

def create_grade_name(request):
    if request.POST:
        form = GradeNameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/grade-names')
    else:
        form = GradeNameForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_grade_name.html', args)

def view_all_grade_names(request):
    template_name = "view_all_grade_names.html"
    gradenames = GradeName.objects.all()
    return render_to_response(template_name, {'gradenames':gradenames})

def view_grade_name(request, pk):
    template_name = "view_grade_name.html"
    gradename = GradeName.objects.get(pk=pk)
    return render_to_response(template_name, {'gradename':gradename})