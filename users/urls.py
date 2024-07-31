from django.urls import path
from .views import search_schol
from .views import home, profile, RegisterView
from .views import generic_view,agriculture_view,search_view

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('generic/', generic_view, name='generic'),
    path('agriculture/', agriculture_view, name='agriculture'),
    path('search/', search_view, name='search'),
    path('search_schol/', search_schol, name='search_schol'),
]
