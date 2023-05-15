from django.shortcuts import render,redirect
from .models import House,Renter,Enviroment,Service,Users,Transaction
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
@login_required(login_url='user_login')
def index(request):
    exisitHouses = House.objects.filter(status=0)
    deleteHouses = House.objects.filter(status=1)

    exisiRenters = Renter.objects.filter(status=0)
    deleteRenters = Renter.objects.filter(status=1)

    exisiEnviroment = Enviroment.objects.filter(status=0)
    deleteEnviroment = Enviroment.objects.filter(status=1)

    exisiSerService =Service.objects.filter(status=0)
    deleteSerService =Service.objects.filter(status=1)

    totalAmmount = Transaction.objects.aggregate(Sum('price'))['price__sum']

    evc = Transaction.objects.filter(account='EVC Plus').aggregate(Sum('price'))['price__sum']
    cash = Transaction.objects.filter(account='Cash').aggregate(Sum('price'))['price__sum']
    merchant = Transaction.objects.filter(account='Merchent').aggregate(Sum('price'))['price__sum']

    topTransaction = Transaction.objects.all().order_by('-id')[:5]
    topEnviroment = Enviroment.objects.all().order_by('-id')[:5]

    totalUsers = User.objects.all()

    # print(merchant)

    

    data = {
        'countExistHouses':exisitHouses.count(),
        'countdeletetHouses':deleteHouses.count(),
        'countExisttRenters':exisiRenters.count(),
        'countdeletetRenters':deleteRenters.count(),
        'countExistEnviroment':exisiEnviroment.count(),
        'countdeletetEnviroment':deleteEnviroment.count(),
        'countExistSerService':exisiSerService.count(),
        'countdeletetSerService':deleteSerService.count(),
        'totalUsers':totalUsers.count(),
        'totalAmount':totalAmmount,
        'topTransaction':topTransaction,
        'topEnviroment':topEnviroment,
        'EvcAccount':evc,
        'CashAccount':cash,
        'MerchantAccount':merchant,

        }
    return render(request, 'main.html',data)

# @login_required(login_url='user_login')
def user_login(request):
     if request.user.is_authenticated:
        # messages.info(request, 'alredy login')
        return redirect(index)
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info( request, 'User or Password are Incorrect.')
            return render(request,'index.html')

     return render(request,'index.html')















