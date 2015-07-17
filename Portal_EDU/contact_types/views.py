from forms import ContactTypeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import ContactType

# Create your views here.
def create_contact_type(request):
    if request.POST:
        form = ContactTypeForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/contact-types')
    else:
        form = ContactTypeForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_contact_type.html', args)

def view_all_contact_types(request):
    template_name = "view_all_contact_types.html"
    contacttypes = ContactType.objects.all()
    return render_to_response(template_name, {'contacttypes':contacttypes})

def view_contact_type(request, pk):
    template_name = "view_contact_type.html"
    contacttype = ContactType.objects.get(pk=pk)
    return render_to_response(template_name, {'contacttype':contacttype})