from django.urls import path
from .views import home, profile, RegisterView
from .views import generic_view,agri_vet_view, comp_math_view, sci_view, art_design_view, engin_tech_view, health_med_view, humanities_view, law_view, fitness_view, social_comms_view, trav_tourism_view
from . import views
from django.urls import path

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('generic/', generic_view, name='generic'),
    path('agri_vet/', agri_vet_view, name='agri_vet'),
    path('comp_math/', comp_math_view, name='comp_math'),
    path('sci/', sci_view, name='sci'),
    path('art_design/', art_design_view, name='art_design'),
    path('engin_tech/', engin_tech_view, name='engin_tech'),
    path('health_med/', health_med_view, name='health_med'),
    path('humanities/', humanities_view, name='humanities'),
    path('law/', law_view, name='law'),
    path('fitness/', fitness_view, name='fitness'),
    path('social_comms/', social_comms_view, name='social_comms'),
    path('trav_tourism/', trav_tourism_view, name='trav_tourism'),
    ]
