import { Component } from '@angular/core';
import { LoginComponent } from '../paginas/login/login.component';
import { RegistroComponent } from '../paginas/registro/registro.component';
import { RouterModule } from '@angular/router';
import { InicioComponent } from '../inicio/inicio.component';
import { ChooseComponent } from '../choose/choose.component';
import { RegistroService } from '../servicios/registro.service';

@Component({
  selector: 'app-content-logout',
  standalone: true,
  imports: [LoginComponent,RegistroComponent,RouterModule,InicioComponent,ChooseComponent],
  templateUrl: './content-logout.component.html',
  styleUrl: './content-logout.component.scss'
})
export class ContentLogoutComponent {

}

