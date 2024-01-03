import { Injectable } from '@angular/core';
import { DTO_Productoo } from '../paginas/mas-vendidos/mas-vendidos.component';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})
export class MasVendidosService {

  constructor(private http: HttpClient) { }

  public GetProducts():Observable<any>{ 
    
    return this.http.get("localhost:8001"); 
  }

  public PostProduct(nombre: DTO_Productoo):Observable<any>{
    return this.http.post("localhost:8001", JSON.stringify(nombre)); 
  }
}
