import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';
import { CookieStorageService } from './cookie-storage.service';
import { OtpRequestResponse, OtpVerificationResponse } from '../interfaces/responses/models';
import { OtpRequest, OtpVerificationRequest } from '../interfaces/requests/models';



@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = environment.apiUrl;
  public userDetail: any

  constructor(private http: HttpClient, private localStorageService: CookieStorageService) { }

  private createCompleteUrl(path: string): string {
    return `${this.apiUrl}${path}`;
  }

  requestOtpForUser(phone_number: Number): Observable<OtpRequestResponse> {
    let complete_url = this.createCompleteUrl('auth/user');
    let otpRequest: OtpRequest = { "phone_number": phone_number.toString(), "country_code": "+91" };
    return this.http.post<OtpRequestResponse>(complete_url, otpRequest);
  }

  verifyOtp(state_token: string, otp: string): Observable<OtpVerificationResponse> {
    let params = new HttpParams().set("state_token", state_token)
    let complete_url = this.createCompleteUrl(`auth/${state_token}`);
    let otpVerification: OtpVerificationRequest = { "otp": otp, "state_token": state_token };
    return this.http.post<OtpVerificationResponse>(complete_url, otpVerification);
  }

  isUserLoggedIn(): boolean {
    return this.localStorageService.getUser() !== "";
  }

  setUser(user: string): void {
    this.localStorageService.setUser(user);
  }

  setToken(token: string): void {
    this.localStorageService.setToken(token);
  }

  getUserDetail() {
    return this.localStorageService.getUserDetail();
  }

  setUserDetail(user: any) {
    this.localStorageService.setUserDetail(user);
  }

  getUserId() {
    const userDetail = this.localStorageService.getUserDetail();
    const user_id = userDetail?.user_id;
    console.log("user_id", user_id);

    return user_id;

  }

  getImageLogo(user_id: string): Observable<Blob> {
    let complete_url = this.createCompleteUrl(`users/${user_id}/logo`);
    return this.http.get<Blob>(complete_url, { responseType: 'blob' as 'json' });
  }

}
