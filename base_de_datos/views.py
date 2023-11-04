from django.shortcuts import render
from .models import Vendedor, User, Cliente
from django.http import JsonResponse
from django.forms.models import model_to_dict
import requests
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json

#Obtener un vendedor por id:
def obtener_vendedor(request, id_user):
    try:
        usuario = User.objects.get(id=id_user)
        vendedores = Vendedor.objects.all()
        vendedor = None
        for i in vendedores:
            if i.user.id == id_user:
                vendedor = i
                break
        #print(vendedores)
        if vendedor:
            vendedor_dict = model_to_dict(vendedor)
            return JsonResponse(vendedor_dict)
        else:
            return JsonResponse({"error": "El usuario no es un vendedor"})
        return JsonResponse(vendedor)
    except User.DoesNotExist:
        return JsonResponse({"error":"El usuario no existe"})

def obtener_cliente_datos_bancarios(request, id_cliente): #Usuario que es cliente
    try:
        usuarios = User.objects.get(id=id_cliente)

        clientes = Cliente.objects.all()
        cliente = None
        for i in clientes:
            if i.user.id == id_cliente:
                cliente = i
        
        return JsonResponse({
            "message":"exito",
            "status":True,
            "numero de cuenta": cliente.cuenta_bancaria,
            "exp month": cliente.exp_month,
            "exp year" : cliente.exp_year
        })
    except User.DoesNotExist:
        return JsonResponse({
            "message":"No existe el usuario \nError de seguridad",
            "status":False
        })
@csrf_exempt
def autenticar_usuario(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = User.objects.filter(username=username).first()
        if user is not None:
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                try:
                    cliente = Cliente.objects.get(user=authenticated_user)
                    user_type = "c"
                except Cliente.DoesNotExist:
                    try:
                        vendedor = Vendedor.objects.get(user=authenticated_user)
                        user_type = 'v'
                    except Vendedor.DoesNotExist:
                        user_type = "0"
                if user_type == "c":
                    datos_salida_user = {
                        "username" : authenticated_user.username,
                        "id" : authenticated_user.id,
                        "numero_clave" : cliente.numero_clave,
                        "cuenta_bancaria" : cliente.cuenta_bancaria,
                        "exp_month" : cliente.exp_month,
                        "exp_year" : cliente.exp_year,
                        "user_type" : user_type
                    }
                elif user_type == "v":
                    datos_salida_user = {
                        "username" : authenticated_user.username,
                        "id" : authenticated_user.id,
                        "numero_clave" : vendedor.numero_clave,
                        "Clabe" : vendedor.Clabe,
                        "cuenta_bancaria" : vendedor.cuenta_bancaria,
                        "exp_month" : vendedor.exp_month,
                        "exp_year" : vendedor.exp_year,
                        "stripe_secret_key" : vendedor.stripe_secret_key,
                        "stripe_publishable_key" : vendedor.stripe_publishable_key,
                        "disponibilidad" : vendedor.disponibilidad,
                        "estrellas_prom" : vendedor.estrellas_prom,
                        "user_type" : user_type
                    }
                else:
                    datos_salida_user = {
                        "username" : authenticated_user.username,
                        "id" : authenticated_user.id,
                        "user_type" : user_type
                    }
                return JsonResponse({
                       'message': 'Usuario autenticado en Dealer',
                       'status': True,
                       'datos_user' : datos_salida_user
                   })
            else:
                return JsonResponse({
                       'message': 'Usuario o contraseña incorrectos',
                       'status': False,
                   })
        else:
            return JsonResponse({
                       'message': 'Usuario inexistente',
                       'status': False,
                   })
    except json.JSONDecodeError:
            # Error en el formato JSON
            return JsonResponse({
                'message': 'Error en el formato JSON',
                'status': False,
            })

    except Exception as e:
            # Manejo de otras excepciones
        return JsonResponse({
            'message': 'Error interno del servidor: {}'.format(str(e)),
            'status': False,
        })
