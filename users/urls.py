from django.urls import path
from .views import home, profile, RegisterView
from .views import generic_view,agri_vet_view
from . import views
from django.urls import path

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('generic/', generic_view, name='generic'),
    path('agri_vet/', agri_vet_view, name='agri_vet'),
    ]
