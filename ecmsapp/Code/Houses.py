from django.shortcuts import render,redirect,HttpResponse
from ecmsapp.models import House
from django.http import JsonResponse

# Create your views here.


def house(request):
    
    houses = House.objects.filter(status=0) 
    context = {'data': houses}

    # if request.method == 'POST':
    #     new_district = request.POST['district']
    #     new_type = request.POST['type']
    #     new_houseno = request.POST['houseno']
    #     new_status = request.POST['status']

    #     if new_district != "" and new_type != "" and new_houseno != "" and new_status != "":
    #         add_house = House(district=new_district, type=new_type, houseno=new_houseno, status=new_status)
    #         add_house.save()
    #     else:
    #         print("bad")

        
    return render(request,'Enviroment/house.html',context)



def createHouse(request):
    if request.method == 'POST':
        new_district = request.POST['district']
        new_type = request.POST['type']
        new_houseno = request.POST['houseno']
        new_status = request.POST['status']

        if new_district != "" and new_type != "" and new_houseno != "" and new_status != "":
            add_house = House(district=new_district, type=new_type, houseno=new_houseno, status=new_status)
            add_house.save()
            isError = True
            return HttpResponse(isError)
        else:
            isError = False
            return HttpResponse(isError)



def update_house(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        district = request.POST.get('district')
        type = request.POST.get('type')
        houseno = request.POST.get('houseno')

        
        houseUpdate = House.objects.get(id=id)

        houseUpdate.district = district
        houseUpdate.type = type
        houseUpdate.houseno = houseno

        houseUpdate.save()

        isError = False
        if isError:
            message = "Failure updating"
            return HttpResponse(message)
        else:
            message = "Successfully Update"
            return HttpResponse(message)

def delete_house(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        status = request.POST.get('status')

        
        houseUpdate = House.objects.get(id=id)

        houseUpdate.status = status

        houseUpdate.save()

        isError = False
        if isError:
            message = "Failure Deleting"
            return HttpResponse(message)
        else:
            message = "Successfully Deleted"
            return HttpResponse(message)
    




def fetch_data(request):
    
    data = House.objects.filter(status=0)
    result=[]
    for row in data:
        result.append(row)
    print(result)
    return JsonResponse(result, safe=False)
