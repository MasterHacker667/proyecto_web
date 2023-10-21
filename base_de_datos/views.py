from django.shortcuts import render
from .models import Vendedor, User
from django.http import JsonResponse
from django.forms.models import model_to_dict
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