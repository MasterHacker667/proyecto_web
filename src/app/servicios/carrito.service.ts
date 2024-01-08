import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DTO_Producto } from '../paginas/principal/principal.component';
import { BehaviorSubject } from 'rxjs';
import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})
export class CarritoService {

  constructor(private http: HttpClient) { }

  private productos: any[] = [];
  private productosSubject = new BehaviorSubject<any[]>([]);

  addToCart(product: DTO_Producto):Observable<any> {
    return this.http.post("https://dummyjson.com/products/add", JSON.stringify(product));
  }

  getItems():Observable<any> {
    return this.http.get("https://dummyjson.com/products");
  }

  // eliminarProducto(index: number) {
  //   const url = https://dummyjson.com/products/delete/${index};
  //   return this.http.delete(url);
  // }
  eliminarProducto(index: number) {
    this.productos.splice(index, 1);
    this.productosSubject.next([...this.productos]);
  }

}