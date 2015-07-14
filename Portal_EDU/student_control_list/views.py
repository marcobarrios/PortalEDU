from forms import StudentControlListForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_student_control_list(request):
    if request.POST:
        form = StudentControlListForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = StudentControlListForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_student_control_list.html', args)