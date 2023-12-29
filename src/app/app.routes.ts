import { Routes } from '@angular/router';
import { LoginComponent } from './paginas/login/login.component';
import { MasVendidosComponent } from './paginas/mas-vendidos/mas-vendidos.component';
import { OfertasComponent } from './paginas/ofertas/ofertas.component';
import { PrincipalComponent } from './paginas/principal/principal.component';
import { CarritoComponent } from './paginas/carrito/carrito.component';

export const routes: Routes = [
    { path: 'principal', component: PrincipalComponent},
    { path: 'ofertas', component: OfertasComponent},
    { path: 'mas-vendidos', component: MasVendidosComponent},
    { path: 'login', component: LoginComponent},
    { path: 'carrito', component: CarritoComponent}
];

