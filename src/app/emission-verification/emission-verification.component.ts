import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { CertificateVerificationData } from '../interfaces/responses/models';
import { Validators } from '@angular/forms';

@Component({
  selector: 'app-emission-verification',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, HttpClientModule],
  templateUrl: './emission-verification.component.html',
  styleUrl: './emission-verification.component.css'
})
export class EmissionVerificationComponent {

  companyName: string | null = null;
  startDate: string | null = null;
  endDate: string | null = null;
  verificationMessage: string | null = null;
  buttonText: string = "Verify";


  verificationForm = this.formBuilder.group({
    certificateNumber: ['', Validators.required],
    carbonEmission: ['', Validators.required]
  })

  constructor(private formBuilder: FormBuilder, private http: HttpClient) { }

  resetResponseProperties() {
    this.companyName = null;
    this.startDate = null;
    this.endDate = null;
  }

  onSubmit() {
    console.warn(this.verificationForm.value);

    if (this.verificationForm.invalid) {
      this.verificationMessage = 'Please fill in all required fields.';
      this.resetResponseProperties();
      this.buttonText = "Try Again";
      return;
    }

    const certificateNumber = String(this.verificationForm.value.certificateNumber);
    const carbonEmission = Number(this.verificationForm.value.carbonEmission);

    if (isNaN(carbonEmission)) {
      this.verificationMessage = 'Please enter a number for the carbon emission.';
      this.resetResponseProperties();
      this.buttonText = "Try Again";
      return;
    }

    const payload: CertificateVerificationData = {
      certificateNumber,
      carbonEmission
    }

    this.http.post<CertificateVerificationData>('http://127.0.0.1:8000/api/v1/verify', payload).subscribe({
      next: (response: CertificateVerificationData) => {
        if (response.status === 'Verified') {
          this.verificationMessage = 'Verified';
          this.companyName = response.companyName!;
          this.startDate = response.startDate!;
          this.endDate = response.endDate!;
          this.buttonText = "Check Another Certificate";
        } else {
          this.verificationMessage = 'Not Verified';
          this.resetResponseProperties();
          this.buttonText = "Try Again";
        }
      },
      error: error => {
        console.error('Error verifying certificate:', error);
        this.verificationMessage = 'An Error Occured';
        this.resetResponseProperties();
        this.buttonText = "Try Again";
      }
    })
  }
}
