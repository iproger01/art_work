from django.urls import path
from .import views

urlpatterns = [
    path("", views.ArtworkView.as_view()),
    path("<slug:slug>/",views.ArtworkDetailView.as_view(), name = "artwork_detail"),
    path("review/<int:pk>/",views.AddReview.as_view(), name = "add_review"),

]