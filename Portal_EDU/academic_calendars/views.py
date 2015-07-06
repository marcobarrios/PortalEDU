from forms import AcademicCalendarForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_academic_calendar(request):
    if request.POST:
        form = AcademicCalendarForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = AcademicCalendarForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_academic_calendar.html', args)