from django.urls import path
from generales import views

#Create your urls with generales
urlpatterns = [
    path('', views.index, name='index'),
]
