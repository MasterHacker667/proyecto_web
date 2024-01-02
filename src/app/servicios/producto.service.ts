import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DTO_Producto } from '../paginas/principal/principal.component';
import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  constructor(private http: HttpClient) { }

  public GetProducts():Observable<any>{ 
    
    return this.http.get("localhost:8001"); //url del puerto de Productos
  }

  public PostProduct(nombre: DTO_Producto):Observable<any>{
    return this.http.post("https://dummyjson.com/products/add", JSON.stringify(nombre)); //deberia ponerse el puero 8001?
  }
}