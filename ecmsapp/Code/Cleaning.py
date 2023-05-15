from django.shortcuts import render,redirect,HttpResponse
from ecmsapp.models import Service,Enviroment,House
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.




@login_required(login_url='user_login')
def cleaning(request):
    district =House.objects.values('district').distinct()
    
    enviroments = Enviroment.objects.filter(status=0)
    cleaning = Service.objects.filter(status=0)
    context = {
        'enviroData':enviroments,
        'serviceData':cleaning,
        'district':district
    }

    if request.method == 'POST':
        new_enviroments = request.POST['enviroment']
        new_date = request.POST['date']
        new_status = request.POST['status']

        if new_enviroments != "" and new_date != "" and new_status != "":
            add_services = Service(date=new_date,status=new_status,enviroment_id=new_enviroments)
            add_services.save()
    return render(request,'Enviroment/cleaning.html',context)


