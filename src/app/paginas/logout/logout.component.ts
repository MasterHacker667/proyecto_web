import { Component } from '@angular/core';

@Component({
  selector: 'app-logout',
  standalone: true,
  imports: [],
  templateUrl: './logout.component.html',
  styleUrl: './logout.component.scss'
})

export class LogoutComponent {
  cerrarSesion() {
    window.location.href = '/login';
  }
  volver() {
    window.location.href = '/inicio';
  }

}




