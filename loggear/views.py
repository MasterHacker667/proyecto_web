from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json
import requests
import random
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def loggearse(request):
    data_body = json.loads(request.body)
    data_usuario = {
        "password": data_body["password"],
        "is_superuser": data_body["is_superuser"],
        "username": data_body["username"],
        "first_name": data_body["first_name"],
        "last_name": data_body["last_name"],
        "email": data_body["email"],
        "is_staff": data_body["is_staff"],
        "is_active": data_body["is_active"],
        "date_joined": data_body["date_joined"]
    }
    response_user = requests.post("http://localhost:8000/api/user/", json= data_usuario)
    if(data_body["tipo_cuenta"] == "c"):
        data_ultimo_user = requests.get("http://localhost:8000/api/user/")
        data_ultimo_user1 = data_ultimo_user.json()
        ultimo_usuario = data_ultimo_user1[-1]
        ultimo_usuario_id = ultimo_usuario.get("id")
        data_cliente = {
            "numero_clave": data_body["numero_clave"],
            "Clabe": data_body["Clabe"],
            "cuenta_bancaria": data_body["cuenta_bancaria"],
            "exp_month": data_body["exp_month"],
            "exp_year": data_body["exp_year"],
            "user": ultimo_usuario_id,
            "foto_perfil": 1
        }
        response_cliente = requests.post("http://localhost:8000/api/clientes/", json= data_cliente)
    else:
        data_ultimo_user = requests.get("http://localhost:8000/api/user/")
        data_ultimo_user1 = data_ultimo_user.json()
        ultimo_usuario = data_ultimo_user1[-1]
        ultimo_usuario_id = ultimo_usuario.get("id")
        data_vendedor = {
            "user_id" : ultimo_usuario_id,
            "numero_clave" : data_body["numero_clave"],
            "Clabe": data_body["Clabe"],
            "cuenta_bancaria": data_body["cuenta_bancaria"],
            "exp_month": data_body["exp_month"],
            "exp_year": data_body["exp_year"],
            "cvc" : data_body["cvc"],
            "client_id_paypal" : data_body["client_id_paypal"],
            "client_secret_paypal" : data_body["client_secret_paypal"],
            "stripe_secret_key" : data_body["stripe_secret_key"],
            "stripe_publishable_key" : data_body["stripe_publishable_key"],
            "disponibilidad" : False,
            "estrellas_prom" : data_body["estrellas_prom"],
            "foto_perfil_id" : 1,
        }
    return JsonResponse({
        "message" : "Logrado",
        "user" : ultimo_usuario_id,
        "status" : True
    })