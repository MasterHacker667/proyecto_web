import { Component } from '@angular/core';
import { RegistroVendedorService } from '../../servicios/vendedor-registro.service';

@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.scss'
})
export class VendedorRegistroComponent {
  nombre: string = '';
  apellido: string = '';
  correo: string = '';
  username: string = '';
  password: string = '';

  constructor(private vendedorRegistroService: RegistroVendedorService) {}

  registrarUsuario() {
    const nuevoUsuario = {
      nombre: this.nombre,
      apellido: this.apellido,
      correo: this.correo,
      username: this.username,
      password: this.password,
    };

    this.vendedorRegistroService.registrarUsuario(nuevoUsuario).subscribe(
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