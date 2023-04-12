from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request,'accounts/register.html')

def forgot(request):
    return render(request,'accounts/forgot.html')

def all_users(request):
    return render(request,'accounts/all_users.html')


def admins(request):
    return render(request,'accounts/admins.html')


def staffs(request):
    return render(request,'accounts/staff.html')


def clients(request):
    return render(request,'accounts/clients.html')


def permissions(request):
    return render(request,'accounts/permissions.html')


def groups(request):
    return render(request,'accounts/groups.html')


def roles(request):
    return render(request,'accounts/roles.html')


def house(request):
    return render(request,'house.html')


def house_holder(request):
    return render(request,'house_holder.html')


def district(request):
    return render(request,'district.html')


def cleaning(request):
    return render(request,'cleaning.html')


def district_cleaned(request):
    return render(request,'district_cleaned.html')


def reports(request):
    return render(request,'reports.html')


def Payment_Method(request):
    return render(request,'Payment_Method.html')


def Transaction(request):
    return render(request,'Transaction.html')


def Reports2(request):
    return render(request,'Reports2.html')

