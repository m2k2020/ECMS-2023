from django.shortcuts import render,redirect,HttpResponse
from ecmsapp.models import Service,Enviroment,House
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.




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


