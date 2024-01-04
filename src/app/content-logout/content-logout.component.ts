import { Component } from '@angular/core';
import { LoginComponent } from '../paginas/login/login.component';
import { RegistroComponent } from '../paginas/registro/registro.component';
import { RouterModule } from '@angular/router';
import { InicioComponent } from '../inicio/inicio.component';
import { ChooseComponent } from '../choose/choose.component';
import { RegistroVendedorComponent } from '../paginas/registro-vendedor/registro-vendedor.component';

@Component({
  selector: 'app-content-logout',
  standalone: true,
  imports: [LoginComponent,RegistroComponent,RouterModule,
    RegistroVendedorComponent,InicioComponent,ChooseComponent,RegistroVendedorComponent],
  templateUrl: './content-logout.component.html',
  styleUrl: './content-logout.component.scss'
})
export class ContentLogoutComponent {

}

