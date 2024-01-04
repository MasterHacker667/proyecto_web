import { Component } from '@angular/core';


@Component({
  selector: 'app-choose',
  standalone: true,
  imports: [],
  templateUrl: './choose.component.html',
  styleUrl: './choose.component.scss'
})
export class ChooseComponent {

  clienteRegistro() {
    window.location.href = '/registro';
  }
  
  vendedorRegistro() {
    window.location.href = '/registro-vendedor';
  }
}



