from django.shortcuts import render,redirect,HttpResponse
from ecmsapp.models import Enviroment,House,Renter
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
import json

# Create your views here.


@login_required(login_url='user_login')
def enviroment(request):
    houses = House.objects.filter(status=0)
    renters = Renter.objects.filter(status=0)
    enivroments = Enviroment.objects.filter(status=0)
    context = {
        'houseData': houses,
        'renterData': renters,
        'enviromentData':enivroments
    }
    return render(request,'Enviroment/enviroment.html',context)

@login_required(login_url='user_login')
def createEnviroment(request):
    if request.method == 'POST':
        new_house = request.POST['houseno']
        new_renter = request.POST['renter']
        new_date = request.POST['regoster_date']
        new_status = request.POST['status']

        if new_house != "" and new_renter != "" and new_date != "" and new_status != "":
            # print(f"{new_date} {new_status} {new_house} {new_renter}")
            add_environment = Enviroment(register_date=new_date,status=new_status,house_id=new_house,renter_id=new_renter,)
            add_environment.save()
            isError = True
            return HttpResponse(isError)
        else:
            isError = False
            return HttpResponse(isError)
        
@login_required(login_url='user_login')
def get_environment(request):
    if request.method == "GET":
        env_id = request.GET.get('id')
        env = Enviroment.objects.get(id=env_id)
        data = {
            'env_id': env.id,
            'renter_name': env.renter.name,
            'renter_id': env.renter.id,
            'house_id': env.house.id,
            'house_no': env.house.houseno
        }
        return JsonResponse(data)

        # singleEnviroment = Enviroment.objects.filter(id=env_id).all()
        # for env in singleEnviroment:
        #     print(env.id, env.renter.name, env.house.houseno)
        # data = {'env':singleEnviroment}
        # data = json.dumps(singleEnviroment)
        # print(singleEnviroment)
        # return JsonResponse(data, safe=False)
        # return HttpResponse("succes")