
from forms import SectionForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Section

# Create your views here.

def create_section(request):
    if request.POST:
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/sections')
    else:
        form = SectionForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_section.html', args)

def view_all_sections(request):
    template_name = "view_all_sections.html"
    sections = Section.objects.all()
    return render_to_response(template_name, {'sections':sections})

def view_section(request, pk):
    template_name = "view_section.html"
    section = Section.objects.get(pk=pk)
    return render_to_response(template_name, {'section':section})