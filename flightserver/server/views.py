from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Flight, Specification


# Create your views here.
def home(request):
    return JsonResponse({'foo': 'bar'})


@csrf_exempt
def form(request):
    if request.method == 'POST':
        print("Request: ", request.POST)
        form_data = request.POST.dict()
        s = Specification(program=form_data['program'])
        s.save()
        f = Flight(
            msn=form_data['msn_data'],
            fprogram=s,
            harness_length=form_data['harness_data'],
            gross_weight=form_data['weight_data'],
            atmospheric_pressure=form_data['pressure_data'],
            room_temperature=form_data['temp_data'],
            airport=form_data['airport_data'],
            fuelcap_left=form_data['feul_cap_left_data'],
            fuelcap_right=form_data['feul_cap_right_data'],
            fuelquant_left=form_data['feul_qua_left_data'],
            fuelquant_right=form_data['feul_qua_right_data'],
            max_altitude=form_data['altitude_data'],
            flight_no=form_data['flight_data']
        )
        f.save()
        print("Object: ", f)
        return JsonResponse({'Success': 'True'})
    else:
        return JsonResponse({'GET': 'Request'})


def search(request):
    return JsonResponse({})
