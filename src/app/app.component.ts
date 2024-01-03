import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
 import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './comun/header/header.component';
import { FooterComponent } from './comun/footer/footer.component';
import { ContentComponent } from './content/content.component';
import { HttpClientModule } from '@angular/common/http';
import { ProductoService } from './servicios/producto.service';
import { OfertasService } from './servicios/ofertas.service';
import { MasVendidosService } from './servicios/mas-vendidos.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderComponent, FooterComponent, ContentComponent, HttpClientModule], 
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [ProductoService,OfertasService,MasVendidosService] 
})
export class AppComponent {

}