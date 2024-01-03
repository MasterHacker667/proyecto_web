import { Component } from '@angular/core';
import { ProductoService } from '../../servicios/producto.service';



/*
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
*/
export interface Imagenes_Productos {
  id:number,
  id_imagen:number,
  id_producto:number
}

@Component({
  selector: 'app-prinicipal',
  standalone: true,
  imports: [],
  templateUrl: './principal.component.html',
  styleUrl: './principal.component.scss'
})
export class PrincipalComponent {
  public lista: DTO_Producto[] = [];
  constructor(private pService: ProductoService){
    pService.GetProducts().subscribe(result => {
      // console.log(result);
      this.lista = result.products;

      pService.PostProduct(this.lista[0]).subscribe(result => {
        console.log(result);
      });
    });
  }
}
// ESTO SE VA A CAMBIAR POR EL DTO COMENTADO ABAJO, solo lo deje asi para ver que funcione
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