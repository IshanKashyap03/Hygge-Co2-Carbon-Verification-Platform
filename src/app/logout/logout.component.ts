import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { CookieStorageService } from '../services/cookie-storage.service';

@Component({
  selector: 'app-logout',
  standalone: true,
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css'],
  imports: [RouterModule]
})
export class LogoutComponent {
  public hygge_name: string = "";

  constructor(private router: Router, private cookieStorageService: CookieStorageService) { }

  ngOnInit() {
    this.hygge_name = this.cookieStorageService.getUser();
  }

  logout() {
    console.log("logout");
    this.cookieStorageService.clear()
    this.router.navigate(['/login']);
  }


}
