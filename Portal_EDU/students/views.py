from django.contrib.auth.forms import UserCreationForm
from forms import StudentForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.

def new_student(request):
	if request.method == 'POST':
		form_new_student = StudentForm(request.POST)
		form_new_user = UserCreationForm(request.POST)
		if form_new_user.is_valid and form_new_student.is_valid:
			form_new_user.save()
			form_new_student.save()
			return HttpResponseRedirect('/')
	else:
		form_new_student = StudentForm()
		form_new_user = UserCreationForm()

	return render_to_response('new_student.html', { 'form_new_user':form_new_user, 'form_new_student':form_new_student}, context_instance = RequestContext(request))

