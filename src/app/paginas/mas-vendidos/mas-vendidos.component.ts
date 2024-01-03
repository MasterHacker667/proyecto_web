import { Component } from '@angular/core';
import { MasVendidosService } from '../../servicios/mas-vendidos.service';

@Component({
  selector: 'app-mas-vendidos',
  standalone: true,
  imports: [],
  templateUrl: './mas-vendidos.component.html',
  styleUrl: './mas-vendidos.component.scss'
})
export class MasVendidosComponent {
  public lista: DTO_Productoo[] = [];
  constructor(private pService: MasVendidosService){
    pService.GetProducts().subscribe(result => {
        // console.log(result);
      this.lista = result.products;
  
      pService.PostProduct(this.lista[0]).subscribe(result => {
        console.log(result);
      });
    });
  }
}

export interface DTO_Productoo{ 
  id:number,
  nombre:string,
  categoria:string,
  descripcion:number,
  color:number,
  precio:number,
  tamano:number
}