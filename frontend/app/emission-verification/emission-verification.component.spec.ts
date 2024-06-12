import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EmissionVerificationComponent } from './emission-verification.component';

describe('EmissionVerificationComponent', () => {
  let component: EmissionVerificationComponent;
  let fixture: ComponentFixture<EmissionVerificationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EmissionVerificationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EmissionVerificationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
