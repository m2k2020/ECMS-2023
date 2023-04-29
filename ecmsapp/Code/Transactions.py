from django.shortcuts import render,redirect
from models import Renter
from django.http import JsonResponse

# Create your views here.


def Transaction(request):
    return render(request,'Enviroment/Transaction.html')