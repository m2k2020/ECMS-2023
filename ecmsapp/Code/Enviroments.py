from django.shortcuts import render,redirect
from ecmsapp.models import Enviroment,House,Renter
from django.http import JsonResponse

# Create your views here.



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
