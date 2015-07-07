from forms import GradeNameForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_grade_name(request):
    if request.POST:
        form = GradeNameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GradeNameForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_grade_name.html', args)