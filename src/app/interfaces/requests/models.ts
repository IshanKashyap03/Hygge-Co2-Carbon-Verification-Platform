export interface OtpRequest {
  phone_number: string;
  country_code: string;
}

export interface OtpVerificationRequest {
  otp: string;
  state_token: string;
}

