import { ActivatedRouteSnapshot, CanActivateFn, Router, RouterStateSnapshot } from '@angular/router';
import { inject } from '@angular/core';
import { CookieStorageService } from '../services/cookie-storage.service';

export const authGuard: CanActivateFn = (route: ActivatedRouteSnapshot, state: RouterStateSnapshot) => {
  if (!inject(CookieStorageService).getToken()) {
    return inject(Router).createUrlTree(['/', 'login'])
  }
  return true;
};
