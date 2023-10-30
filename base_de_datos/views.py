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
                return JsonResponse({
                       'message': 'Usuario autenticado en Dealer',
                       'status': True,
                   })
            else:
                return JsonResponse({
                       'message': 'Usuario p contraseña incorrectos',
                       'status': False,
                   })
        else:
            return JsonResponse({
                       'message': 'Usuario o contraseña incorrectos',
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
