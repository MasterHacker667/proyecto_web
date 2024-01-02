import { Injectable } from '@angular/core';
import { DTO_Producto } from '../paginas/principal/principal.component';

@Injectable({
  providedIn: 'root'
})
export class CarritoService {
  public lista: DTO_Producto[] = [];

  addToCart(product: DTO_Producto) {
    this.lista.push(product);
  }

  getItems() {
    return this.lista;
  }

  clearCart() {
    this.lista = [];
    return this.lista;
  }

  constructor() { }
}
