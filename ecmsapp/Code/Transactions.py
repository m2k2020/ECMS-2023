from django.shortcuts import render,redirect
from ecmsapp.models import Service,Transaction
from django.http import JsonResponse

# Create your views here.


def transaction(request):
    serviceList = Service.objects.filter(status=0)
    data = {
        'dataService': serviceList
    }
    return render(request,'Enviroment/Transaction.html',data)


def makePayment(request):

    if request.method == 'POST':
        pay_service = request.POST.get('service')
        accounts = request.POST.get('account')
        pay_date = request.POST.get('date')
        pay_price = 5
        pay_status = 0

        msg = ""

        servid = Service.objects.get(id=pay_service)

        msg += f"Renter : {servid.enviroment.renter.name}-{servid.enviroment.renter.tell}\n"
        msg += f"House : {servid.enviroment.house.district}-{servid.enviroment.house.houseno}-({servid.enviroment.house.type})\n"
        msg += f"Account : {accounts}\n"
        msg += f"date : {pay_date} and Price {pay_price}\n"

        print(msg)
        addrow = Transaction(service=servid,date=pay_date,status=pay_status,account=accounts,price=pay_price)
        addrow.save()
        if addrow:
            servid.process = "Paid"
            servid.save()
            response = {
                'success': True,
                'message': f'Your transaction has been created by {msg}',
                'error': f'Not Saved by {msg}'
            }
            return JsonResponse(response)
        else:
            response = {
                'error': True,
                'message': f'Not Saved by {msg}'
            }
            return JsonResponse(response)
