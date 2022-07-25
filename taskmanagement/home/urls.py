from django.urls import path
from . import views

# a simple home url pattern
urlpatterns = [
    path('', views.HomeView.as_view()),
]
