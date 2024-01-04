from django.shortcuts import render
from django.http import JsonResponse
import random
from django.contrib.auth.hashers import make_password
from django.views import View
import json
import requests
import string
from django.views.decorators.csrf import csrf_exempt
def contruit_nu_ped():
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':', ',', '.', '<', '>', '/', '?']
    abc = list(string.ascii_letters)
    numbers = [1,2,3,4,5,6,7,8,9,0]
    lista = []
    for i in symbols:
        lista.append(i)
    for i in abc:
        lista.append(i)
    for i in numbers:
        lista.append(i)
    no = random.randint(1,10000000)
    #Constructing varnumber
    numer = ""
    largo = random.randint(1,24)
    i = 0
    while (i<largo):
        cosa = random.randint(0, len(lista)-1)
        numer = numer + str(lista[cosa])
        i+=1
        
    if not numer:
        numer = str(no)
    return numer
@csrf_exempt
def agregar_carrito_ped(request):
    #Esta vista solo se encargará de crear los pedidos de los productos para los clientes, no debería mostrar mucho más que la información que se ha metido
    data_body = json.loads(request.body.decode("utf-8"))
    #Primero debemos obtener los productos de dicho carrito
    try:
        lista_prod_car = []
        response = requests.get("http://localhost:8000/api/producto_carrito/")
        response = response.json()
        for i in response:
            if i["id_Carrito"] == data_body["idcarrito"]:
                lista_prod_car.append(i["id_Producto"])
        #Obtenemos el id del cliente al que le pertenece el carrito:
        response = requests.get("http://localhost:8000/api/clientes_carritos/")
        response = response.json()
        id1 = 0
        for i in response:
            if i["id_carrito"] == data_body["idcarrito"]:
                id1 = i["id_cliente"]
                break
        
        #Una vez que ya tenemos los productos que están en ese carrito, debemos saber que vendedores los tienen
        #Buscamos en productos vendedores o algo asi los vendedores por sus productos
        #Que vendedor vende que:
        response = requests.get("http://localhost:8000/api/producto_vendedor/")
        response = response.json()
        prod_vende = []
        for i in lista_prod_car: #Recorremos los productos del carrito
            for j in response: #Recorremos cada relacion de producto vendedor
                if i == j["id_Producto"]:
                    prod_vende.append({
                        "producto" : i,
                        "vendedor" : j["id_Vendedor"]
                    })
        #Para este punto ya obtuvimos todos los productos que vende cada vendedor
        #Ahora vamos a ir haciendo varios pedidos en la bd así:
        responseNo = requests.get("http://localhost:8000/api/pedidos/")
        responseNo = responseNo.json()
        mens = ""
        if id1 != 0:
            for i in prod_vende:
                #Construyendo numero de pedido:

                no = contruit_nu_ped()
                ii = 0
                while(ii<len(responseNo)):
                    if responseNo[ii]["No_Pedido"] == no:
                        ii = 0
                        no = contruit_nu_ped()
                    ii+=1
                data_meter = {
                    "No_Pedido": no,
                    "entregado": False,
                    "id_cliente": id1,
                    "id_vendedor": i["vendedor"],
                    "id_Carrito": data_body["idcarrito"]
                }
                response = requests.post("http://localhost:8000/api/pedidos/", json=data_meter)
                mens = response.status_code
            ultimate_data = {
                "message" : "Data inserted succesfully",
                "mensaje" : mens,
                "status" : True
            }
            #Eliminando el carrito en cuestión:
            #response = requests.post("http://127.0.0.1:8010/del_carr/", json={"carrito" : data_body["idcarrito"]})

            return JsonResponse(ultimate_data, safe=False)
        else:
            return JsonResponse({
            "message" : "No. Pedido no genereted",
            "status" : False
        })
        
    except Exception as e:
        return JsonResponse({
            "message" : str(e),
            "status" : False
        })
@csrf_exempt
def ver_pedidos(request): #Vista para que un vendedor vea los pedidos que le hicieron
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        pedidos = requests.get("http://localhost:8000/api/pedidos/")
        pedidos = pedidos.json()
        elegidos = []
        for i in pedidos:
            if i["id_vendedor"] == data_body["id_vendedor"]:
                elegidos.append(i)
        #elegidos contiene los pedidos del vendedor, así que ahora lo recorreremos buscando los carritos que buscamos
        carros = requests.get("http://localhost:8000/api/carrito/")
        carros = carros.json()
        nCarros = None
        for i in elegidos: #Recorremos cada pedido
            for j in carros:
                if j["id"] == i["id_Carrito"]:
                    nCarros = j #Aqui estamos teniendo el carro que pertenecen a los pedidos
        
        #Ahora vamos a recorrer cada carro y vamos a obtener los productos de cada carro
        carros11 = []
        prod = requests.get("http://localhost:8000/api/producto_carrito/")
        prod = prod.json()
        productos = []
        for j in prod:
            if nCarros["id"] == j["id_Carrito"]:
                productos.append(j["id_Producto"])
                #Aqui encontramos los productos que pertenecen al carro

        carros11 = {
            "Carro":nCarros["id"],
            "Productos" : productos
        }
        #Para este punto ya tenemos todos los ids de los productos que tiene un carro, ahora debemos buscar sus datos
        resp_prod = requests.get("http://localhost:8000/api/productos/")
        resp_prod = resp_prod.json()
        carros12 = []
        cuentas = 0.0
        for i in carros11["Productos"]:
            for j in resp_prod:
                if i == j["id"]:
                    carros12.append(j)
                    cuentas += j["precio"]
        
        #Aqui ya tenemos los productos relacionados con cada carrito, que a su vez están relacionados con cada pedido
        #Debemos ahora saber, con el id de cada cliente, dónde se encuentra el salón e institución
        salones = []
        for i in elegidos: #Vamos a recorrer cada pedido para obtener los salones de cada cliente
            response = requests.post("http://127.0.0.1:3030/ver_inst_cliente/", json = {"idcliente" : i["id_cliente"]})
            response = response.json()
            salones.append(response)
        #Ahora buscamos los datos del cliente en cuestion (que esta en cada pedido)
        response = requests.get("http://localhost:8000/api/clientes/")
        response = response.json()
        clientes = []
        for i in elegidos:
            for j in response:
                if i["id_cliente"] == j["id"]:
                    clientes.append(j)
                    break
        clientes2 = []
        for i in clientes:
            response = requests.post("http://localhost:8000/verUsers_id/", json={
                "id_user" : i["user"]
            })
            response = response.json()
            #clientes2.append(response)
            clientes2.append({
                "username" : response[0]["fields"]["username"],
                "firstname" : response[0]["fields"]["first_name"],
                "lastname" : response[0]["fields"]["last_name"],
                "email" : response[0]["fields"]["email"]
            })
        final = []
        ii = 0
        largo = len(elegidos)
        while(ii<largo):
            final.append({
                "pedido" : elegidos[ii],
                "salones" : salones[ii],
                "cliente" : clientes2[ii],
                "productos" : carros12,
                "total a cobrar" : "$" + str(cuentas)
            })
            ii+=1
        #Ahora vamos a ir recorriendo los productos de los pedidos para saber que vamos a entregar y cuanto
        
        return JsonResponse(final, safe= False)
    except Exception as e:
        return JsonResponse({
            "message" : str(e),
            "status" : False
        })
@csrf_exempt
def eliminar_ped(request):
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        response = requests.get("http://127.0.0.1:8000/delete/pedido/"+str(data_body["id_pedido"]))
        if response.status_code == 200 or response.status_code == 201:
            return JsonResponse({
                "message" : "Pedido eliminado",
                "status" : True
            })
        else:
            return JsonResponse({
                "message" : "Pedido NO eliminado",
                "status" : True
            })
    except Exception as e:
        return JsonResponse({
            "message" : str(e),
            "status" : True
        })

@csrf_exempt
def verPed_cliente(request):
    data_body = json.loads(request.body.decode("utf-8"))
    try:
        response = requests.get("http://localhost:8000/api/pedidos/")
        response = response.json()
        elegidos = []
        for i in response:
            if i["id_cliente"] == data_body["id_cliente"]:
                elegidos.append(i)
        return JsonResponse({
            "cliente" : data_body["id_cliente"],
            "pedidos" : elegidos
        })
    except Exception as e:
        return JsonResponse({
            "message" : str(e),
            "status" : False
        })