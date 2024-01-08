import { TestBed } from '@angular/core/testing';
import { RegistroVendedorService } from './vendedor-registro.service';

describe('VendedorRegistroService', () => {
  let service: RegistroVendedorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RegistroVendedorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
