from forms import ClassRoomForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_class_room(request):
    if request.POST:
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = ClassRoomForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_class_room.html', args)