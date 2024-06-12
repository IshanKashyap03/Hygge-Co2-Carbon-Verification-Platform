// TODO: Split the CertificateVerificationData into request and response
export interface CertificateVerificationData {
  certificateNumber: string,
  carbonEmission: number,
  companyName?: string,
  status?: string
  startDate?: string,
  endDate?: string,
}
export interface CertificateData {
  certificateNumber: string,
  companyName: string,
  startDate: Date,
  endDate: Date,
  issueDate: Date,
  carbonEmission: number
}
export interface UserModel {
  phone_number: string;
  name: string;
  email: string;
  user_id: string;
  logo_url: string;
  country: string;
  city: string;
  address: string;
}
export interface OtpVerificationResponse {
  state_token: string;
  attemptsRemaining: number;
  createdTime: string;
  status: string;
  statusDesc: string;
  session_token: string;
  refreshToken: string;
  user: UserModel;
}

export interface OtpRequestResponse {
  state_token: string;
  attemptsRemaining: number;
  createdTime: string;
  status: string;
  statusDesc: string;
}
