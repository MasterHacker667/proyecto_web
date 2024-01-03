import { Injectable } from '@angular/core';
import { DTO_Ofertas } from '../paginas/ofertas/ofertas.component';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { stringify } from 'querystring';


@Injectable({
  providedIn: 'root'
})

@Injectable({
  providedIn: 'root'
})
export class OfertasService {

  constructor(private http: HttpClient) { }

  public GetOfertas():Observable<any>{ 
    
   // return this.http.get("localhost:8001"); //url del puerto de Productos
    return this.http.get("https://dummyjson.com/products/category/smartphones"); // Lo deje asi para ver que funcionara =)
  }

  public PostOferta(nombre: DTO_Ofertas):Observable<any>{
    return this.http.post("https://dummyjson.com/products/add", JSON.stringify(nombre)); //deberia ponerse el puero 8001
  }
}