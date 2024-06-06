import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms'
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { HTTP_STATUS_CODES, MAX_PHONE_DIGITS, OTP_LENGTH } from '../constants'
import { ViewChildren, QueryList, ElementRef } from '@angular/core';
import { Subscription } from 'rxjs';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule]
})
export class LoginComponent implements OnInit {
  reactiveForm!: FormGroup
  protected maxPhoneDigits = MAX_PHONE_DIGITS;
  protected otpLength = OTP_LENGTH;
  protected otp_requested: boolean = false;
  protected is_loading: boolean = false;
  protected is_authorized: boolean = true;
  protected otp_error: boolean = false;
  protected max_attempts_reached: boolean = false;
  protected unexpected_error: boolean = false;
  protected otpParts = ['otp1', 'otp2', 'otp3', 'otp4', 'otp5', 'otp6'];
  @ViewChildren('otpInput') otpInputs!: QueryList<ElementRef>;
  private state_token: string = "";
  private subscriptions: Subscription[] = [];


  constructor(
    private auth: AuthService,
    private route: Router) {
    if (this.auth.isUserLoggedIn()) {
      this.route.navigateByUrl('/');
    }

  }

  ngOnInit() {
    this.loadValidators();
    this.subscribePhoneNumberChanges();
  }

  ngOnDestroy() {
    this.subscriptions.forEach(subscription => subscription.unsubscribe());
  }

  protected get get_phone_number() { return this.reactiveForm.get('phone_number') }

  private loadValidators() {
    this.reactiveForm = new FormGroup({
      phone_number: new FormControl(null, [
        Validators.required,
        Validators.pattern('^[0-9]{10}$')
      ]),
    });
    for (let i = 1; i <= OTP_LENGTH; i++) {
      const controlName = `otp${i}`;
      this.reactiveForm.addControl(
        controlName,
        new FormControl(null, Validators.required)
      );
    }
  }

  protected onOtpInputKeyUp(event: KeyboardEvent, nextInputIndex: number, prevInputIndex: number) {
    if (event.key !== 'Backspace' && event.key !== "Tab") {
      this.otp_error = false
      if ((<HTMLInputElement>event.target).value && nextInputIndex !== -1) {
        this.otpInputs.toArray()[nextInputIndex].nativeElement.focus();
      }
    } else {
      if (prevInputIndex !== -1) {
        this.otpInputs.toArray()[prevInputIndex].nativeElement.focus();
      }
    }
  }

  private setRequestOtpState() {
    this.is_loading = false;
    this.otp_requested = true;
    this.resetOtp();
  }

  private setRequestPhoneState() {
    this.max_attempts_reached = false;
    this.is_loading = false;
    this.otp_requested = false;
    this.otp_error = false;
    this.unexpected_error = false;
    this.resetOtp();
    this.get_phone_number!.reset();
  }

  private resetOtp() {
    this.otpParts.forEach(name => {
      this.reactiveForm.get(name)?.reset();
    })
  }

  private subscribePhoneNumberChanges() {
    this.subscriptions.push(
      this.get_phone_number!.valueChanges.subscribe((newValue) => {
        if (newValue && newValue.toString().length !== 0) {
          this.is_authorized = true;
          this.max_attempts_reached = false;
        }
      })
    );
  }

  private processError(error: any) {
    this.setRequestPhoneState();
    if (error.status === HTTP_STATUS_CODES.UNAUTHORIZED) {
      this.is_authorized = false;
    }
    else {
      this.unexpected_error = true;
    };
  };

  protected onOtpSubmit() {
    let otpParts = this.otpParts.map((name) => this.reactiveForm.get(name)?.value);
    this.is_loading = true;
    let otp: string = otpParts.join('');

    this.subscriptions.push(
      this.auth.verifyOtp(this.state_token, otp).subscribe({
        next: (res) => {
          if (res.status === "SUCCESS") {
            this.auth.setToken(res.session_token);
            this.auth.setUser(res.user?.name)
            this.auth.setUserDetail(res?.user);
            this.route.navigateByUrl('/');
            return;
          }
          if (res.status === "OTP_RESTRICTED") {
            this.setRequestPhoneState();
            this.max_attempts_reached = true;
            return;
          }
          this.setRequestOtpState();
          this.otp_error = true;
        },
        error: (error) => {
          this.processError(error);
        },
        complete: () => {

        }
      })
    );
  }

  protected onPhoneNumberSubmit() {
    this.is_loading = true;
    let phoneNumber: Number = this.get_phone_number?.value;

    this.subscriptions.push(
      this.auth.requestOtpForUser(phoneNumber).subscribe({
        next: (res) => {
          if (res.status === "RESTRICTED") {
            this.setRequestPhoneState();
            this.max_attempts_reached = true;
            return;
          }
          this.setRequestOtpState();
          this.state_token = res.state_token;
        },
        error: (error) => {
          this.processError(error);
        },
        complete: () => {

        }
      })
    );
  }
}

