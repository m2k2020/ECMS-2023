from django.shortcuts import render,redirect
from .models import House,Renter,Enviroment,Service,Users,Transaction
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'main.html')















