import { Injectable } from '@angular/core';
import { UserModel } from '../interfaces/responses/models';
import { CookieService } from 'ngx-cookie-service';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CookieStorageService {

  public project_prefix = environment.PROJECT_PREFIX;

  constructor(private cookieService: CookieService) { }

  getUser(): string {
    let item = this.cookieService.get(this.project_prefix + 'hygge_user') || "";
    if (item == "" || item == "undefined") { return "" }
    return item;
  }

  setUser(user: string): void {
    this.cookieService.set(this.project_prefix + 'hygge_user', user);
  }

  getToken(): string {
    let item = this.cookieService.get(this.project_prefix + 'token') || "";
    if (item == "" || item == "undefined") { return "" }
    return item;
  }

  setToken(token: string): void {
    this.cookieService.set(this.project_prefix + 'token', token);
  }

  setUserDetail(user: UserModel): void {
    this.cookieService.set(this.project_prefix + 'userDetail', JSON.stringify(user));
  }

  getUserDetail() {
    let userString = this.cookieService.get(this.project_prefix + 'userDetail');
    if (!userString) return null
    let user = JSON.parse(userString);
    return user;
  }

  clear(): void {
    this.cookieService.deleteAll();
  }
}
