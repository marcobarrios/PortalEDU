from forms import GenreForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from .models import Genre

# Create your views here.

def create_genre(request):
    if request.POST:
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/genres')
    else:
        form = GenreForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_genre.html', args)

def view_all_genres(request):
    template_name = "view_all_genres.html"
    genres = Genre.objects.all()
    return render_to_response(template_name, {'genres':genres})

def view_genre(request, pk):
    template_name = "view_genre.html"
    genre = Genre.objects.get(pk=pk)
    return render_to_response(template_name, {'genre':genre})