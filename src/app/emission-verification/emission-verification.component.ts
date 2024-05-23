import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { CertificateVerificationData } from './certificate-verificationData-interface';
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
  verificationMessage: string | null = null;
  buttonText : string = "Verify";


  verificationForm = this.formBuilder.group({
    certificateNumber: ['', Validators.required],
    carbonEmission : ['', Validators.required]
  })

  constructor(private formBuilder: FormBuilder, private http: HttpClient) {}

  onSubmit() {
    console.warn(this.verificationForm.value);

    if (this.verificationForm.invalid) {
      this.verificationMessage = 'Please fill in all required fields.';
      this.companyName = null;
      this.buttonText = "Try Again";
      return;
    }

    const certificateNumber = String(this.verificationForm.value.certificateNumber);
    const carbonEmission = Number(this.verificationForm.value.carbonEmission);

    if (isNaN(carbonEmission)) {
      this.verificationMessage = 'Please enter a number for the carbon emission.';
      this.companyName = null;
      this.buttonText = "Try Again";
      return;
    }

    const payload: CertificateVerificationData = {
      certificateNumber,
      carbonEmission
    }

    this.http.post<CertificateVerificationData>('http://127.0.0.1:8000/api/v1/verify', payload).subscribe({
      next: (response: CertificateVerificationData) =>{
        if (response.status === 'Verified') {
          this.verificationMessage = 'Verified';
          this.companyName = response.companyName!;
          this.buttonText = "Check Another Certificate";
        } else {
          this.verificationMessage = 'Not Verified';
          this.companyName = null;
          this.buttonText = "Try Again";
        }
      }, 
      error: error => {
        console.error('Error verifying certificate:', error);
        this.verificationMessage = 'An Error Occured';
        this.companyName = null;
        this.buttonText = "Try Again";
      }
    })
  }
}
