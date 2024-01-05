import { Component } from '@angular/core';
import { BarraNavComponent } from '../../barra-nav/barra-nav.component';


@Component({
  selector: 'app-header',
  standalone: true,
  imports: [BarraNavComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {

}


