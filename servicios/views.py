from django.shortcuts import render

# Create your views here.
def termsAndConditions(request):
    return render(request, 'termsAndConditions.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def contacts(request):
    return render(request, 'contacts.html')

def securityPolitics(request):
    return render(request, 'securityPolitics.html')