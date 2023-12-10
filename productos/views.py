from django.shortcuts import render

# Create your views here.

#Item Menu
def pageBusines(request):
    return render(request, 'pageBusines.html')

def pageBusinesWithhoutLogin(request):
    return render(request, 'pageBusinesWithhoutLogin.html')

def pageReservations(request):
    return render(request, 'pageReservations.html')

def pageBuyTicket(request):
    return render(request, 'pageBuyTicket.html')

def customerManager(request):
    return render(request, 'customerManager.html')

#About Product
def product(request):
    return render(request, 'product.html')

def buy(request):
    return render(request, 'paymentGateways.html')