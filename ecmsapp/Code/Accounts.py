from django.shortcuts import render,redirect
from ecmsapp.Code import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission

# Create your views here.

@login_required(login_url='user_login')
def logout_view(request):
    logout(request)
    messages.info(
            request, 'Logout!')
    return redirect('user_login')


def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forgot.html')


def staffs(request):
    users = User.objects.all()
    data = {
        'users': users
    }
    return render(request,'accounts/staffs.html',data)
