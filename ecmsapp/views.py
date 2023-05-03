from django.shortcuts import render,redirect
from .models import House,Renter,Enviroment,Service,Users,Transaction
from django.http import JsonResponse

# Create your views here.
def index(request):
    exisitHouses = House.objects.filter(status=0)
    deleteHouses = House.objects.filter(status=1)

    exisiRenters = Renter.objects.filter(status=0)
    deleteRenters = Renter.objects.filter(status=1)

    exisiEnviroment = Enviroment.objects.filter(status=0)
    deleteEnviroment = Enviroment.objects.filter(status=1)

    exisiSerService =Service.objects.filter(status=0)
    deleteSerService =Service.objects.filter(status=1)


    data = {
        'countExistHouses':exisitHouses.count(),
        'countdeletetHouses':deleteHouses.count(),
        'countExisttRenters':exisiRenters.count(),
        'countdeletetRenters':deleteRenters.count(),
        'countExistEnviroment':exisiEnviroment.count(),
        'countdeletetEnviroment':deleteEnviroment.count(),
        'countExistSerService':exisiSerService.count(),
        'countdeletetSerService':deleteSerService.count(),
        }
    return render(request, 'main.html',data)















