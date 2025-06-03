from django.urls import path 
from . import views 

urlpatterns = [
    path("" , views.home, name="homePage"),
    path("menu", views.menu, name="menuPage"),
    path("rrethnesh", views.rrethnesh, name="rrethneshPage"),
    path("footer", views.footer, name="footerPage"),
    path("base", views.base, name="basePage"),
    path("navbar", views.base, name="navbarPage"),
    path('kontakt/', views.kontakt_view, name='kontaktPage'),
    path('kontakt/faleminderit/', views.kontakt_faleminderit, name='kontakt_faleminderit'),
    path('porositonline/', views.porositonline, name='porositonlinePage'),
    
]

