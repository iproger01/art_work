from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import ReviewForm

class ArtworkView(ListView):
    '''Работы художников'''
    model = Artworks
    queryset = Artworks.objects.filter(draft=False)
    template_name = "artworks/artworks_list.html"


class ArtworkDetailView(DetailView):
    '''Детальная информация по работе'''
    model = Artworks
    template_name = "artworks/artworks_detail.html"
    slug_field = "url"

class AddReview(View):
    '''Отзывы'''
    model = Artworks
    def post(self,request,pk):
        form = ReviewForm(request.POST)
        artwork = Artworks.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.artworks = artwork
            form.save()
        return redirect(artwork.get_absolute_url())


