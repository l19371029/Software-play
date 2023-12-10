from django.urls import path
from productos import views

urlpatterns = [
    #Item Menu
    path('productos-negocios-iniciar-sesion/', views.pageBusines, name="pageBusines"),
    path('productos-negocios/', views.pageBusinesWithhoutLogin, name="pageBusinesWithhoutLogin"),
    path('productos-reservacion/', views.pageReservations, name="pageReservations"),
    path('productos-pagina-compra-boleto/', views.pageBuyTicket, name="pageBuyTicket"),
    path('productos-gestionamiento-clientes/', views.customerManager, name="customerManager"),

    #About Product
    path('descripcion/', views.product, name="product"),

    #Api Payment gateways
    path('Compra/', views.buy, name="Buy"),
]