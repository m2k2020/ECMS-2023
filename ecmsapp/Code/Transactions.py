from django.shortcuts import render,redirect
from ecmsapp.models import Service
from django.http import JsonResponse

# Create your views here.


def Transaction(request):
    serviceList = Service.objects.filter(status=0)
    data = {
        'dataService': serviceList
    }
    return render(request,'Enviroment/Transaction.html',data)