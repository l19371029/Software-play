from django.urls import path
from api import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
]
