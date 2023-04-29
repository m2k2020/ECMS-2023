from django.shortcuts import render,redirect
from ecmsapp.models import Service,Enviroment
from django.http import JsonResponse

# Create your views here.



def reports(request):
    return render(request,'Enviroment/reports.html')



def Reports2(request):
    return render(request,'Enviroment/Reports2.html')
