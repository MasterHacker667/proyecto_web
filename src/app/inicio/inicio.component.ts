import { Component } from '@angular/core';
import { HeaderComponent } from '../comun/header/header.component';
import { ContentComponent } from '../content/content.component';
import { FooterComponent } from '../comun/footer/footer.component';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-inicio',
  standalone: true,
  imports: [HeaderComponent,ContentComponent,FooterComponent,HttpClientModule,CommonModule, RouterOutlet],
  templateUrl: './inicio.component.html',
  styleUrl: './inicio.component.scss',
  providers: [HttpClientModule] 
})
export class InicioComponent{

}


