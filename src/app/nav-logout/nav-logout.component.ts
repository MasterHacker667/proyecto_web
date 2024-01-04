import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'

@Component({
  selector: 'app-nav-logout',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './nav-logout.component.html',
  styleUrl: './nav-logout.component.scss'
})
export class NavLogoutComponent {
  menus : string[] = ["Iniciar Sesión","Registrarse"];
}



