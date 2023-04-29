from django.shortcuts import render,redirect
from models import House,Renter,Enviroment,Service,Users,Transaction
from django.http import JsonResponse

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forgot.html')


def staffs(request):
    return render(request,'accounts/staffs.html')
