import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-emission-verification',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './emission-verification.component.html',
  styleUrl: './emission-verification.component.css'
})
export class EmissionVerificationComponent {
  private mockCertificateNumber = '121';
  private mockCarbonEmission = '121';
  private mockCompanyName = 'Satyam Steel';

  companyName: string | null = null;
  verificationMessage: string | null = null;
  buttonText : string = "Verify";


  verificationForm = this.formBuilder.group({
    certificateNumber: [''],
    carbonEmission : ['']
  })

  constructor(private formBuilder: FormBuilder) {}

  onSubmit() {
    console.warn(this.verificationForm.value);
    if(this.verificationForm.value.certificateNumber === this.mockCertificateNumber && this.verificationForm.value.carbonEmission === this.mockCarbonEmission){
     this.verificationMessage = "Verified";
     this.companyName = this.mockCompanyName;
     this.buttonText = "Check Another Certificate";
    }else{
      this.verificationMessage = "Not Verified";
      this.companyName = null;
      this.buttonText = "Try Again";
    }
  }
}
