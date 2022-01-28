from django.urls import path
from .import views

urlpatterns = [
    path("", views.ArtworkView.as_view()),
    path("filter/", views.FilterArtworkView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("event/", views.EventView.as_view(), name="event"),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/",views.ArtworkDetailView.as_view(), name = "artwork_detail"),
    path("review/<int:pk>/",views.AddReview.as_view(), name = "add_review"),
    path("artist/<str:slug>/", views.ArtistsDetailView.as_view(), name="artist_detail"),


]