import { Component } from '@angular/core';
import { MasVendidosService } from '../../servicios/mas-vendidos.service';
import { HeaderComponent } from '../../comun/header/header.component';

@Component({
  selector: 'app-mas-vendidos',
  standalone: true,
  imports: [HeaderComponent],
  templateUrl: './mas-vendidos.component.html',
  styleUrl: './mas-vendidos.component.scss'
})
export class MasVendidosComponent {
  public lista: DTO_Productoo[] = [];
  constructor(private pService: MasVendidosService){
    pService.GetProducts().subscribe(result => {
      this.lista = result.products;
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