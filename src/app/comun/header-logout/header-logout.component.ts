import { Component } from '@angular/core';
import { NavLogoutComponent } from '../../nav-logout/nav-logout.component';

@Component({
  selector: 'app-header-logout',
  template: `
    <div ngSkipHydration></div>
  `,
  standalone: true,
  imports: [NavLogoutComponent],
  templateUrl: './header-logout.component.html',
  styleUrl: './header-logout.component.scss'
})
export class HeaderLogoutComponent {

}

