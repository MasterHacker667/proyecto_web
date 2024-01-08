import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
 import { RouterOutlet } from '@angular/router';
import { HeaderLogoutComponent } from './comun/header-logout/header-logout.component';
import { FooterComponent } from './comun/footer/footer.component';
import { ContentLogoutComponent } from './content-logout/content-logout.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginService } from './servicios/login.service';
import { HeaderComponent } from './comun/header/header.component';
import { BarraNavComponent } from './barra-nav/barra-nav.component';

@Component({
  selector: 'app-root',
  template: `
    <div ngSkipHydration></div>
  `,
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderLogoutComponent, FooterComponent, ContentLogoutComponent, 
    HttpClientModule, HeaderComponent, BarraNavComponent], 
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [LoginService] 
})

export class AppComponent {
  login: boolean = false;

}