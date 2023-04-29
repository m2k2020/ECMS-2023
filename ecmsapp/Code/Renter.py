from django.shortcuts import render,redirect
from models import Renter
from django.http import JsonResponse

# Create your views here.


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
