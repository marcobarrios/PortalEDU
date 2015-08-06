from forms import ClassRoomForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import ClassRoom
from django.contrib.auth.decorators  import  login_required

# Create your views here.

@login_required(login_url = '/accounts/login/')
def create_class_room(request):
    if request.POST:
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/classrooms')
    else:
        form = ClassRoomForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_class_room.html', args)

@login_required(login_url = '/')
def view_all_classrooms(request):
    template_name = "view_all_classrooms.html"
    classrooms = ClassRoom.objects.all()
    return render_to_response(template_name, {'classrooms':classrooms})

@login_required(login_url = '/')
def view_classroom(request, pk):
    template_name = "view_classroom.html"
    classroom = ClassRoom.objects.get(pk=pk)
    return render_to_response(template_name, {'classroom':classroom})