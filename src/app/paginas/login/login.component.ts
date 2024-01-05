import { Component } from '@angular/core';
import { LoginService } from '../../servicios/login.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  public username!:string;
  public password!: string;

    constructor(private uService: LoginService, private ruteador: Router){
    }
    public Iniciar(){

      this.uService.LoginUser(this.username,this.password).subscribe(resultado => {
        this.ruteador.navigate(["inicio"]);
      });
    }
}

export interface DTO_Usuario {
  id: number,
  username: string,
  email: string,
  firstName: string,
  lastName: string,
  gender: string
  image: string,
  token: string
}