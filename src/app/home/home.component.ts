import { Component } from '@angular/core';
import { EmissionVerificationComponent } from '../emission-verification/emission-verification.component';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [EmissionVerificationComponent, NavbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
