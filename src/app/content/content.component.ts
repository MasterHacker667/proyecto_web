import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PrincipalComponent } from '../paginas/principal/principal.component';
import { OfertasComponent } from '../paginas/ofertas/ofertas.component';
import { MasVendidosComponent } from '../paginas/mas-vendidos/mas-vendidos.component';
import { LoginComponent } from '../paginas/login/login.component';

@Component({
  selector: 'app-content',
  standalone: true,
  imports: [RouterModule,PrincipalComponent,OfertasComponent,MasVendidosComponent,LoginComponent],
  templateUrl: './content.component.html',
  styleUrl: './content.component.scss'
})
export class ContentComponent {

}

