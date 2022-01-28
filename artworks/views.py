from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import ReviewForm, RaitingForm

class CategoryYear():
    """Категории и года создания"""
    def get_category(self):
        return Category.objects.all()

    def get_years(self):
        return Artworks.objects.filter(draft=False).values("year").distinct("year")

class ArtworkView(CategoryYear, ListView):
    '''Работы художников'''
    model = Artworks
    queryset = Artworks.objects.filter(draft=False)
    template_name = "artworks/artworks_list.html"
    paginate_by = 2


class ArtworkDetailView(CategoryYear, DetailView):
    '''Детальная информация по работе'''
    model = Artworks
    template_name = "artworks/artworks_detail.html"
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["star_form"] = RaitingForm()
        context["form"] = ReviewForm()
        return context



class ArtistsDetailView(CategoryYear, DetailView):
    '''Вывод информации о художнике'''
    model = Artists
    template_name = "artworks/artist.html"
    slug_field = "surname"

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


class FilterArtworkView(CategoryYear, ListView):
    """Фильтр Картин"""
    paginate_by = 2
    def get_queryset(self):
        queryset = Artworks.objects.filter(
            Q(year__in=self.request.GET.getlist("year"))|
            Q(category__in=self.request.GET.getlist("category"))
                                           )
        return queryset

class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RaitingForm(request.POST)
        if form.is_valid():
            Raiting.objects.update_or_create(
                ip=self.get_client_ip(request),
                artworks_id=int(request.POST.get("artwork")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

class Search(ListView):
    """Поиск картины"""
    paginate_by = 2
    def get_queryset(self):
        return Artworks.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super(Search, self).get_context_data(*args,**kwargs)
        context["q"] = f'&q={self.request.GET.get("q")}'
        return context

class EventView(ListView):
    '''Постеры событий'''
    model = Event
    template_name = "artworks/event.html"
    paginate_by = 3
