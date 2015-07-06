from forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def create_contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_contact.html', args)