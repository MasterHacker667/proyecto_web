from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
import requests
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def pago_stripe(request):#Esta funcion debe recibir por post el id_user del cliente y el id_user del vendedor
    try:
        
        data = json.loads(request.body)
        #Obteniendo los datos necesario de dealer:
        response_dealer = requests.get(f"http://127.0.0.1:8000/cliente/id_cliente/{data['id_cliente_user']}")
        datos_cliente = response_dealer.json()
        return JsonResponse({
            "message":"Logrado",
            "status":True,
            "objetos_recuperados": datos_cliente
        })
    except json.JSONDecodeError:
        return JsonResponse({
            "message":"Error de codificacion",
            "status":False
        })
