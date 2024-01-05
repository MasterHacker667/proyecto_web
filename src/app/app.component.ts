import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
 import { RouterOutlet } from '@angular/router';
import { HeaderLogoutComponent } from './comun/header-logout/header-logout.component';
import { FooterComponent } from './comun/footer/footer.component';
import { ContentLogoutComponent } from './content-logout/content-logout.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginService } from './servicios/login.service';

@Component({
  selector: 'app-root',
  template: `
    <div ngSkipHydration></div>
  `,
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderLogoutComponent, FooterComponent, ContentLogoutComponent, 
    HttpClientModule], 
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [LoginService] 
})
export class AppComponent {

}