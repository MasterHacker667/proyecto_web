import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-barra-nav',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './barra-nav.component.html',
  styleUrl: './barra-nav.component.scss'
})
export class BarraNavComponent {
  menus : string[] = ["Principal","Ofertas","Más Vendidos","Cerrar Sesión",""];
}



