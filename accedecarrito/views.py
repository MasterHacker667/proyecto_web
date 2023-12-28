from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views import View
import json
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def crearCarritos(request):
    data_body = json.loads(request.body.decode("utf-8")) 
    #Verificamos que el producto lo tenga disponible el cliente:
    obtenido = False
    try:
        response_prod_vende = requests.get("http://localhost:8000/api/producto_vendedor/")
        response_prod_vende = response_prod_vende.json()
        #Ahora, una vez tenemos la informacion, debemos ver si TODOS los productos estan disponibles en ese vendedor:
        tot_prod_disp = 0
        cosa = False
        for i in response_prod_vende:
            for j in data_body["productos"]:
                if i["id_Producto"] == j:
                    tot_prod_disp+=1
                if data_body["tot_articulos"] == tot_prod_disp:
                    cosa = True
                    break
            if cosa:
                break
        #ahora debemos determinar si se obtuvieron todos los productos, si no es así, se manda un json y si sí se cumple, se continua con el proceso
        if cosa==False:
            return JsonResponse({
                "message" : "One or more products missing",
                "status":False
            }, safe=False)
        else:
            #Aqui se continua con el proceso, ya que sabemos que tenemos todos los articulos
            #Ahora que sabemos que todos los articulos están, debemos Crear el carrito

            #Sacando el total de los precios:
            tot_prec = 0
            response = requests.get("http://localhost:8000/api/productos/")
            response = response.json()
            productos = []
            for i in data_body["productos"]:
                for j in response:
                    if j["id"] == i:
                        productos.append(j)
                        tot_prec = tot_prec + j["precio"]
                        break

            data_carr = {
                "No_Articulos" : data_body["tot_articulos"],
                "precio_total" : tot_prec, #Este dato lo sacamos arriba de esto con varios get's
                "nombre" : data_body["nombre"]
            }
            response = requests.post("http://localhost:8000/api/carrito/", json = data_carr)
            data_carr = {
                "No_Articulos" : data_body["tot_articulos"],
                "precio_total" : tot_prec, #Este dato lo sacamos arriba de esto con varios get's
                "nombre" : data_body["nombre"],
                "productos" : productos
            }
            #Ya tenemos el carrito, ahora a establecer una relacion entre los productos y el carrito en la bd:
            #Primero debemos reobtener el carrito con los datos que tenemos:
            response = requests.get("http://localhost:8000/api/carrito/")
            response = response.json()
            carro = {}
            for i in response:
                if i["No_Articulos"] == data_carr["No_Articulos"] and i["precio_total"] == data_carr["precio_total"] and i["nombre"] == data_carr["nombre"]:
                    carro = i
                    break
            #Encontramos el carrito, ahora debemos establecer un vinculo con los productos haciendo varios post por producto:
            for i in data_body["productos"]:
             
                datos_vinculo = {
                    "id_Carrito" : carro["id"],
                    "id_Producto" : i
                }
                response = requests.post("http://localhost:8000/api/producto_carrito/", json = datos_vinculo)
            #Ahora que tenemos establecido el vinculo entre los productos y el carrito, debemos establecer entre el carrito y el cliente:
            vinculo = {
                "id_carrito" : carro["id"],
                "id_cliente" : data_body["id_cliente"]
            }
            response = requests.post("http://localhost:8000/api/clientes_carritos/", json=vinculo)
            return JsonResponse(data_carr, safe=False)
    except requests.RequestException:
        return JsonResponse({
            "message" : "request error",
            "status" : False
        }, safe= False)
    
@csrf_exempt
def carritos_cliente(request):
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        response = requests.get("http://localhost:8000/api/clientes_carritos/")
        response = response.json()
        carritos_rel = []
        for i in response:
            if i["id_cliente"] == data_body["idcliente"]:
                carritos_rel.append(i)
        #Tenemos solo las relaciones y los id's necesarios, ahora debemos buscar entre los carritos sus metadatos
        response = requests.get("http://localhost:8000/api/carrito/")
        response = response.json()
        carros = []
        for i in carritos_rel:
            for j in response:
                if i["id_carrito"] == j["id"]:
                    carros.append(j)
        #Ya tenemos todos los metadatos de los carros, ahora vamos por los productos que contiene
        response = requests.get("http://localhost:8000/api/producto_carrito/")
        response = response.json()
        productos_carritoid = []
        #Buscando los id's de los productos que estan en cada carrito:
        for i in carros:
            prodids = []
            for j in response:
                if i["id"] == j["id_Carrito"]:
                    prodids.append(j["id_Producto"])
            productos_carritoid.append({
                "carrito" : i,
                "productos" : prodids
            }) 

        #Para este punto tenemos los productos que tiene cada carrito          
        response2 = requests.get("http://localhost:8000/api/productos/")
        response2 = response2.json()
        productos_carritoid2 = []
        for i in productos_carritoid: #Recorremos cada uno de los carritos
            array_prods = []
            for j in i["productos"]: #Recorremos cada id_prod de cada carrito
                for a in response2: #Por cada producto de cada carrito recorremos todos los productos para ver sus datos
                    if a["id"] == j:
                        array_prods.append(a) #Agregamos todo el array de los productos que buscamos por id
                        break
            #Una vez obtenidos los datos de los productos procedemos a reacer el array
            productos_carritoid2.append({
                "carrito" : i["carrito"],
                "productos" : array_prods
            })
        return JsonResponse(productos_carritoid2, safe=False)
    except requests.RequestException:
        return JsonResponse({
            "message" : "request error\nTry again",
            "status" : False
        }, safe= False)

@csrf_exempt
def delete_car(request):
    data_body = json.loads(request.body.decode("utf-8"))
    message_json1 = {"message" : "I don't know, good job?", "status" : True}
    message_json2 = {"message" : "I don't know, good job?", "status" : True}
    message_json3 = {"message" : "I don't know, good job?", "status" : True}
    try:
        response = requests.get("http://localhost:8000/delete_clientes_carritos/"+str(data_body["carrito"]))
        if response.status_code != 200:
            #Ya eliminamos algo de clientes_carritos, ahora falta eliminar de productos_carrito
            message_json1 = {
                "message" : "Failed to delete record in clientes_carritos",
                "status" : False,
                "Error message" : response.status_code
            }
        response = requests.get("http://localhost:8000/delete/delete_productos_carrito/"+str(data_body["carrito"]))
        if response.status_code != 200:
            #Ya eliminamos algo de clientes_carritos, ahora falta eliminar de productos_carrito
            message_json2 = {
                "message" : "Failed to delete record in productos_carritos",
                "status" : False,
                "Error message" : response.status_code
            }
        if message_json1["status"] and message_json2["status"]:
            response = requests.get("http://localhost:8000/delete/delete_carrito/"+str(data_body["carrito"]))
            if response.status_code != 200:
                message_json3 = {
                    "message" : "Failed to delete record in productos_carritos",
                    "status" : False,
                    "Error message" : response.status_code
                }
        else:
            message_json3 = {
                "message" : "Failed to delete record in productos_carritos",
                "status" : False,
                "Error message" : response.status_code
            }
        message_json = {
            "First json" : message_json1,
            "Second json" : message_json2,
            "third json" : message_json3
        }

        return JsonResponse(message_json, safe=False)
    except Exception as e:
        return JsonResponse({
            "message" : "delete request failed",
            "status" : False,
            "Message error" : e
        })
@csrf_exempt
def add_prod_car(request):
    data_body = json.loads(request.body.decode("utf-8"))
    data_n = {
        "id_Carrito" : data_body["id_carrito"] ,
        "id_Producto" : data_body["id_producto"]
    }
    try:
        response = requests.post("http://localhost:8000/api/producto_carrito/", json=data_n)
        #Una vez hecha la relacion debemos buscar el carrito para poder alterar el precio total
        response = requests.get("http://localhost:8000/api/carrito/")
        response = response.json()
        carro1 = {}
        for i in response:
            if i["id"] == data_body["id_carrito"]:
                carro1 = i
                break
        #Tenemos el carrito, ahora debemos encontrar el producto
        response = requests.get("http://localhost:8000/api/productos/")
        response = response.json()
        cosa2 = {}
        for i in response:
            if i["id"] == data_body["id_producto"]:
                cosa2 = i
                break
        #Ya tenemos el producto y el carrito, ahora debemos cambiar el dato en carrito:
        carro1["precio"] = float(carro1["precio_total"]) + float(cosa2["precio"])
        #Ahora debemos alterar el valor de un carrito, pero de eso se encargara dealer, nosotros haremos el json sobre el carrito que debe modificar y el dato:
        dato_mod = {
            "precio_n" : carro1["precio"],
            "id_carrito" : carro1["id"]
        }
        response = requests.post("http://localhost:8000/update/carrito_precio/", json = dato_mod)

        return JsonResponse({
            "message" : "Product added succesfully",
            "status" : True,
            "Thing" : dato_mod
        })
    except Exception as e:
        return JsonResponse({
            "message" : "Post error\nTry again later",
            "status" : False,
            "Error Message" : str(e)
        })