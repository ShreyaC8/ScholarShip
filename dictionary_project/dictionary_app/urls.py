from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_dictionary, name='search_dictionary'),
]