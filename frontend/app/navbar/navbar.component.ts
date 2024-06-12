import { Component } from '@angular/core';
import { LogoutComponent } from '../logout/logout.component';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [LogoutComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

}
