import { Component } from '@angular/core';
import { CarritoService } from '../../servicios/carrito.service';
import { ProductoService } from '../../servicios/producto.service';
import { HeaderComponent } from '../../comun/header/header.component';
@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [HeaderComponent],
  templateUrl: './carrito.component.html',
  styleUrl: './carrito.component.scss'
})
export class CarritoComponent {
  public lista: DTO_Producto[] = [];
  constructor(private carritoService: CarritoService){
    carritoService.getItems().subscribe(result => {
      this.lista = result.products;
    });
    carritoService.addToCart(this.lista[0]).subscribe(result => {
      console.log(result);
    });
  }
  eliminarProducto(index: number) {
    this.carritoService.eliminarProducto(index);
    console.log(this.carritoService.getItems());
  }
}


export interface DTO_Producto{ 
  id:number,
  title:string,
  description:string,
  price:number,
  discountPercentage:number,
  rating:number,
  stock:number,
  brand:string,
  category:string,
  thumbnail:string,
  images:string[]
}

/*
export interface DTO_Producto{ 
  id:number,
  nombre:string,
  categoria:string,
  descripcion:number,
  color:number,
  precio:number,
  tamano:number
}
*/