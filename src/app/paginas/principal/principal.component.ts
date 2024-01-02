import { Component } from '@angular/core';
import { ProductoService } from '../../servicios/producto.service';
import { CarritoService } from '../../servicios/carrito.service';

@Component({
  selector: 'app-principal',
  standalone: true,
  imports: [],
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.scss'
})



//ME QUEDE EN USAR EL SERVICIO



export class PrincipalComponent {

  public lista: DTO_Producto[] = [];

    constructor(private pService: ProductoService)
    {
      pService.GetProducts().subscribe(result => {
        // console.log(result);
        this.lista = result.products;
  
        pService.PostProduct(this.lista[0]).subscribe(result => {
          console.log(result);
        });
      });
    }

}

export interface DTO_Producto{ 
  id:number,
  nombre:string,
  categoria:string,
  descripcion:number,
  color:number,
  precio:number,
  tamano:number
}

export interface Imagenes_Productos {
  id:number,
  id_imagen:number,
  id_producto:number
}

