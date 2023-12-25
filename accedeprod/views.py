from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views import View
import json
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def agregar_Productos(request):
    response = requests.get('http://localhost:8000/api/productos/')
    if response .status_code == 200:
        bandera = False
        id = 0
        datos_json = response.json()
        data_body = json.loads(request.body.decode('utf-8'))
        for i in datos_json:
            if i["nombre"] == data_body["nombre"] and i["categoria"] == data_body["categoria"] and i["color"] == data_body["color"] and i["tamano"] == data_body["tamano"]:
                bandera = True
                id = i["id"]
                break 
        if bandera:
            datos_a_enviar = {
                "cantidad" : data_body["cantidad"],
                "id_Producto" : id,
                "id_Vendedor" : data_body["id_vendedor"]
            }
            try:
                response = requests.post('http://localhost:8000/api/producto_vendedor/', json=datos_a_enviar)
                datos_json = datos_a_enviar
            except requests.RequestException:
                response = {
                    "message" : "no load data",
                    "status" : False
                }
                datos_json = response
            
        else:
            datos_a_enviar_p = {
                "nombre" : data_body["nombre"],
                "categoria" : data_body["categoria"],
                "descripcion" : data_body["descripcion"],
                "color" : data_body["color"],
                "precio" : data_body["precio"],
                "tamano" : data_body["tamano"]
            }
            try:
                datos_cool = {}
                response1 = requests.post('http://localhost:8000/api/productos/',json=datos_a_enviar_p)
                response2 = requests.get('http://localhost:8000/api/productos/')
                for i in response2.json():
                    if i["nombre"] == datos_a_enviar_p["nombre"] and i["categoria"] == datos_a_enviar_p["categoria"] and i["descripcion"] == datos_a_enviar_p["descripcion"] and i["color"] == datos_a_enviar_p["color"] and i["precio"] == datos_a_enviar_p["precio"] and i["tamano"] == datos_a_enviar_p["tamano"]:
                        datos_cool = i
                        break
                nuevos_d = {
                    "cantidad" : data_body["cantidad"],
                    "id_Producto" : i["id"],
                    "id_Vendedor" : data_body["id_vendedor"]
                }
                response3 = requests.post('http://localhost:8000/api/producto_vendedor/', json=nuevos_d)
                datos_json = nuevos_d
            except requests.RequestException:
                response1 = {
                    "message" : "no load data",
                    "status" : False
                }
        return JsonResponse(datos_json, safe=False)
    else:
        datos_json = {
            "message" : "Bad direction",
            "status" : False
        }

        return JsonResponse(datos_json, safe=False)

@csrf_exempt
def productos_vende(request):
    try:
        data_body = json.loads(request.body.decode('utf-8'))
        response = requests.get('http://localhost:8000/api/producto_vendedor/')
        datos = response.json()
        datos_v = []
        for i in datos:
            if i["id_Vendedor"] == data_body["id_vendedor"]:
                datos_v.append(i)
        productos_vendedor = []
        response = requests.get('http://localhost:8000/api/productos/')
        datos = response.json()
        for i in datos_v:
            for j in datos:
                if i["id_Producto"] == j["id"]:
                    productos_vendedor.append({
                        "nombre": j["nombre"],
                        "categoria": j["categoria"],
                        "descripcion": j["descripcion"],
                        "color": j["color"],
                        "precio": j["precio"],
                        "tamano": j["tamano"],
                        "cantidad": i["cantidad"]
                    })
        
        return JsonResponse(productos_vendedor, safe=False)
    except requests.RequestException:
        return JsonResponse({
            "message" : "no data",
            "status" : False
        }, safe=False)