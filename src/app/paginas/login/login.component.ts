
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  constructor(private router: Router) {}

  login(): void {
    if (this.username === 'esme' && this.password === '123') {
      console.log('check');

      this.router.navigate(['/inicio']);
    } else {
      console.log('no funciono');
    }
  }
}

