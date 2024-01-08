import { Component } from '@angular/core';
import { RegistroService } from '../../servicios/registro.service';
import { HeaderLogoutComponent } from '../../comun/header-logout/header-logout.component';

@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [HeaderLogoutComponent],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.scss'
})
export class RegistroComponent {
  nombre: string = '';
  apellido: string = '';
  correo: string = '';
  username: string = '';
  password: string = '';

  constructor(private registroService: RegistroService) {}

  registrarUsuario() {
    const nuevoUsuario = {
      nombre: this.nombre,
      apellido: this.apellido,
      correo: this.correo,
      username: this.username,
      password: this.password,
    };

    this.registroService.registrarUsuario(nuevoUsuario).subscribe(
      (response) => {
        console.log('Usuario registrado exitosamente:', response);
        // Aquí puedes redirigir a otra página, mostrar un mensaje, etc.
      },
      (error) => {
        console.error('Error al registrar usuario:', error);
      }
    );
  }
}