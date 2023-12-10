from django.urls import path
from servicios import views

urlpatterns = [
    path('Terminos&Condiciones/', views.termsAndConditions, name="termsAndConditions"),
    path('contactos/', views.contacts, name="contacts"),
    path('Acer-de-nosotros/', views.aboutUs, name='aboutUS'),
    path('Politicas-de-Seguridad/', views.securityPolitics, name="securityPolitics"),
]