import { Injectable } from '@angular/core';
import { catchError } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs'; 

import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse,
} from '@angular/common/http';

import { Router } from '@angular/router';
import { CookieStorageService } from '../services/cookie-storage.service';
import { HTTP_STATUS_CODES } from '../constants';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private router: Router, private localStorageService: CookieStorageService) {}

  intercept(
    request: HttpRequest<unknown>,
    next: HttpHandler
  ): Observable<HttpEvent<unknown>> {
    const token = this.localStorageService.getToken();
    if (token) {
      request = request.clone({
        headers: request.headers.set('Authorization', `Bearer ${token}`),
      });
    }
    return next.handle(request).pipe(
      catchError((error: HttpErrorResponse) => {
        console.log(error)
        if (error.status === HTTP_STATUS_CODES.UNAUTHORIZED) {
          this.localStorageService.clear()
          this.router.navigate(['/login']); 
        }
        if (error.status === HTTP_STATUS_CODES.SERVER_ERROR) {
          console.log("server error")
        }
        console.log("throwing error")
        return throwError(() => error); 
      })
    );
  }
}
