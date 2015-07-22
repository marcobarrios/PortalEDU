from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

# Create your views here.
def apolodb_login(request):
	if request.method == 'POST':
		form_login = AuthenticationForm(request.POST)
		if form_login.is_valid:
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password = passwd)
			if access is not None:
				if access.is_active:
					login(request,access)
					return render_to_response("index.html", {})
				else:
					return render_to_response('not_active.html',context_instance=RequestContext(request))
			else:
				return render_to_response('not_user.html', context_instance=RequestContext(request))
	else:
		form_login = AuthenticationForm()
	return render_to_response('login.html', {'form_login':form_login}, context_instance = RequestContext(request))
