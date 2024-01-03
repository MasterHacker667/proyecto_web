from django.shortcuts import render
from django.http import JsonResponse
import random
from django.contrib.auth.hashers import make_password
from django.views import View
import json
import requests
import string
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ver_inst_vendedor(request):
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        response = requests.get("http://localhost:8000/api/vendedor_salones_instituciones/")
        response = response.json()
        elegido = []
        for i in response:
            if i["id"] == data_body["vendedor"]:
                elegido.append(i["id_salones_instituciones"])
        #Con esto ya sabemos a que salones_instituciones pertenece el vendedor, así que toca obtener las instituciones
        response = requests.get("http://localhost:8000/api/salones_instituciones/")
        response = response.json()
        nombre_salones = []
        for i in response:
            for j in elegido:
                if i["id"] == j and i["institucion"] not in nombre_salones:
                    nombre_salones.append(i["institucion"])
        #Una vez que tenemos la institucion la pondremos ahí, pero ahora toca poner lo que este vendedor vende (los productos)
        response = requests.get("http://localhost:8000/api/producto_vendedor/")
        response = response.json()
        productoid = []
        for i in response:
            if i["id_Vendedor"] == data_body["vendedor"]:
                productoid.append({
                    "producto" : i["id_Producto"],
                    "cantidad" : i["cantidad"]
                })
        #Ya tenemos el producto que tiene y cuanto de eso tiene, ahora debemos obtener los datos de ese producto
        response = requests.get("http://localhost:8000/api/productos/")
        response = response.json()
        productos_fin = []
        for i in response:
            for j in productoid:
                if j["producto"] == i["id"] and j["cantidad"] != 0:
                    productos_fin.append({
                        "data_producto" : i,
                        "cantidad" : j["cantidad"]
                    })
        return JsonResponse({
            "productos" : productos_fin,
            "instituciones" : nombre_salones
        }, safe=False)
    except Exception as e:
        JsonResponse({
            "message" : str(e),
            "status" : False
        })



@csrf_exempt
def ver_inst_cliente(request):
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        response = requests.get("http://localhost:8000/api/salones_instituciones_cliente/")
        response = response.json()
        obtener = []
        for i in response:
            if i["id_cliente"] == data_body["idcliente"]:
                obtener.append(i["id_salones_instituciones"])
        #Aqui ya obtuvimos todas las instituciones donde se encuentra el cliente.
        #Ahora debemos obtener los salones donde se encuentra el cliente en cada institucion
        response = requests.get("http://localhost:8000/api/salones_instituciones/")
        response = response.json()
        salon_ins = []
        for i in obtener:
            for j in response:
                if i == j["id"]:
                    salon_ins.append({
                        "institucion" : j["institucion"],
                        "edificio" : j["edificio"],
                        "salon" : j["salon"]
                    })
        return JsonResponse(salon_ins, safe=False)

    except Exception as e:
        return JsonResponse({
            "message" : str(e),
            "status" : False
        })

@csrf_exempt
def agregar_cli(request):
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        #vemos si la institucion existe:
        response = requests.get("http://localhost:8000/api/salones_instituciones/")
        response = response.json()
        bandera = False
        inst = []
        verificar = {
            "institucion" : data_body["institucion"],
            "salon" : data_body["salon"],
            "edificio" : data_body["edificio"]
        }
        for i in response:
            if i["institucion"] == verificar["institucion"] and i["salon"] == verificar["salon"] and i["edificio"] == verificar["edificio"]:
                bandera = True
                inst = i
                break
        if bandera:
            #Aqui pondremos lo que pasa si ya existen los datos
            #Verificamos que haya alguna relacion entre la institucion y el cliente
            bandera = False
            response = requests.get("http://localhost:8000/api/salones_instituciones_cliente/")
            response = response.json()
            for i in response:
                if i["id_salones_instituciones"] == inst["id"] and i["id_cliente"] == data_body["idcliente"]:
                    bandera = True
                    break
            if bandera:
                return JsonResponse({
                    "message" : "El cliente ya tiene registrada esta institucion con el mismo salon y el mismo edificio",
                    "status" : False
                })
            else:
                cosa = {
                    "id_salones_instituciones" : inst["id"],
                    "id_cliente" : data_body["idcliente"]
                }
                response = requests.post("http://localhost:8000/api/salones_instituciones_cliente/", json = cosa)
                return JsonResponse({
                    "message" : "Se realizó solamente la relación, ya que el registro de institucion, salón y edificio ya existían",
                    "status" : True
                })
        else:
            #Aqui lo que pasa si la institucion/salon/edificio no existen
            response = requests.post("http://localhost:8000/api/salones_instituciones/", json={
                "institucion" : data_body["institucion"],
                "salon" : data_body["salon"],
                "edificio" : data_body["edificio"]
            })
            #Ahora rebuscamos este en los registros:
            response = requests.get("http://localhost:8000/api/salones_instituciones/")
            response = response.json()
            cosa_id = 0
            for i in response:
                if i["institucion"] == data_body["institucion"] and i["salon"] == data_body["salon"] and i["edificio"] == data_body["edificio"]:
                    cosa_id = i["id"]
                    break
            #Ahora lo relacionamos con el cliente
            response = requests.post("http://localhost:8000/api/salones_instituciones_cliente/", json = {
                "id_salones_instituciones" : cosa_id,
                "id_cliente" : data_body["idcliente"]
            })
            return JsonResponse({
                "message" : "datos insertados",
                "status" : True
            })

    except Exception as e:
        return JsonResponse({
            "message" : str(e),
            "status" : False
        }, safe=False)
