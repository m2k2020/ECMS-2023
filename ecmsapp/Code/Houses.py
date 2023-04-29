from django.shortcuts import render,redirect
from ecmsapp.models import House
from django.http import JsonResponse

# Create your views here.


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





def fetch_data(request):
    
    data = House.objects.filter(status=0)
    result=[]
    for row in data:
        result.append(row)
    print(result)
    return JsonResponse(result, safe=False)
