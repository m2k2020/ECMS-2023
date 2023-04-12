from django.shortcuts import render,redirect
from .models import House,Renter
from django.http import JsonResponse

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


#region Enviroment


#region House

def house(request):

    
    houses = House.objects.filter(status=0) 
    context = {'data': houses}

    if request.method == 'POST':
        new_district = request.POST['district']
        new_type = request.POST['type']
        new_houseno = request.POST['houseno']
        new_status = request.POST['status']

        if new_district != "" and new_type != "" and new_houseno != "" and new_status != "":
            add_house = House(district=new_district, type=new_type, houseno=new_houseno, status=new_status)
            add_house.save()
        else:
            print("bad")

        
    return render(request,'Enviroment/house.html',context)

def createHouse(request):
    new_district = request.POST['district']
    new_type = request.POST['type']
    new_houseno = request.POST['district']
    new_status = request.POST['status']

    print(new_district, new_type, new_houseno, new_status)


    return redirect('house')

#endregion house


def renter(request):
       
    renters = Renter.objects.filter(status=0)
    context = {'data':renters}

    if request.method == 'POST':
        new_name = request.POST['name']
        new_tell = request.POST['tell']
        new_martial_status = request.POST['martial_status']
        new_status = request.POST['status']

        if new_name != "" and new_tell != "" and new_martial_status != "" and new_status != "":
            add_renter = Renter(name=new_name, tell=new_tell, martial_status=new_martial_status, status=new_status)
            add_renter.save()
    return render(request,'Enviroment/renter.html',context)


def Enviroment(request):
    houses = House.objects.filter(status=0)
    renters = Renter.objects.filter(status=0)
    context = {
        'houseData': houses,
        'renterData': renters
    }
    return render(request,'Enviroment/enviroment.html',context)



def fetch_data(request):
    # data = House.objects.values("id","district","type","houseno")
    data = House.objects.filter(status=0)
    result=[]
    for row in data:
        result.append(row)
    print(result)
    return JsonResponse(result, safe=False)

#endregion


def cleaning(request):
    return render(request,'cleaning.html')


def Enviroment_cleaned(request):
    return render(request,'Enviroment_cleaned.html')


def reports(request):
    return render(request,'reports.html')


def Payment_Method(request):
    return render(request,'Payment_Method.html')


def Transaction(request):
    return render(request,'Transaction.html')


def Reports2(request):
    return render(request,'Reports2.html')

