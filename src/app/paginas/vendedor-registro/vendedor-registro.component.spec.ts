import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VendedorRegistroComponent } from './vendedor-registro.component';

describe('VendedorRegistroComponent', () => {
  let component: VendedorRegistroComponent;
  let fixture: ComponentFixture<VendedorRegistroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VendedorRegistroComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VendedorRegistroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
