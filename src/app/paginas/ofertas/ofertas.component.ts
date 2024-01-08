import { Component } from '@angular/core';
import { OfertasService } from '../../servicios/ofertas.service';
import { HeaderComponent } from '../../comun/header/header.component';
import { ProductoService } from '../../servicios/producto.service';

@Component({
  selector: 'app-ofertas',
  standalone: true,
  imports: [HeaderComponent],
  templateUrl: './ofertas.component.html',
  styleUrl: './ofertas.component.scss'
})
export class OfertasComponent {
  public lista: DTO_Ofertas[] = [];

    constructor(private pOferta: OfertasService)
    {
      pOferta.GetOfertas().subscribe(result => {
        // console.log(result);
        this.lista = result.products;
  
        pOferta.PostOferta(this.lista[0]).subscribe(result => {
          console.log(result);
        });
      });
    }

    agregarAlCarrito(lista:DTO_Ofertas){
      console.log("agregado al carrito:" + lista.title);
    }
  }
/*
  export interface DTO_Ofertas{ 
    id:number,
    nombre:string,
    categoria:string,
    descripcion:number,
    color:number,
    precio:number,
    tamano:number
  }
  */

  export interface DTO_Ofertas{ 
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