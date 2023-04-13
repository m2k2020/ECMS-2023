from django.shortcuts import render,redirect
from .models import House,Renter,Enviroment,Service,Users,Transaction
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


def enviroment(request):
    houses = House.objects.filter(status=0)
    renters = Renter.objects.filter(status=0)
    enivroments = Enviroment.objects.filter(status=0)
    context = {
        'houseData': houses,
        'renterData': renters,
        'enviromentData':enivroments
    }

    if request.method == 'POST':
        new_house = request.POST['houseno']
        new_renter = request.POST['renter']
        new_date = request.POST['regoster_date']
        new_status = request.POST['status']

        if new_house != "" and new_renter != "" and new_date != "" and new_status != "":
            # print(f"{new_date} {new_status} {new_house} {new_renter}")
            add_environment = Enviroment(register_date=new_date,status=new_status,house_id=new_house,renter_id=new_renter,)
            add_environment.save()
    return render(request,'Enviroment/enviroment.html',context)



def fetch_data(request):
    
    data = House.objects.filter(status=0)
    result=[]
    for row in data:
        result.append(row)
    print(result)
    return JsonResponse(result, safe=False)

#endregion


def cleaning(request):
    enviroments = Enviroment.objects.filter(status=0)
    cleaning = Service.objects.filter(status=0)
    context = {
        'enviroData':enviroments,
        'serviceData':cleaning
    }

    if request.method == 'POST':
        new_enviroments = request.POST['enviroment']
        new_date = request.POST['date']
        new_status = request.POST['status']

        if new_enviroments != "" and new_date != "" and new_status != "":
            add_services = Service(date=new_date,status=new_status,enviroment_id=new_enviroments)
            add_services.save()
    return render(request,'Enviroment/cleaning.html',context)




def reports(request):
    return render(request,'Enviroment/reports.html')


def Payment_Method(request):
    return render(request,'Enviroment/Payment_Method.html')


def Transaction(request):
    return render(request,'Enviroment/Transaction.html')


def Reports2(request):
    return render(request,'Enviroment/Reports2.html')

