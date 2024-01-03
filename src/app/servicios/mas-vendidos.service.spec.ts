import { TestBed } from '@angular/core/testing';

import { MasVendidosService } from './mas-vendidos.service';

describe('MasVendidosService', () => {
  let service: MasVendidosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MasVendidosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
