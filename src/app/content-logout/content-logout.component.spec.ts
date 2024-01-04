import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentLogoutComponent } from './content-logout.component';

describe('ContentLogoutComponent', () => {
  let component: ContentLogoutComponent;
  let fixture: ComponentFixture<ContentLogoutComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContentLogoutComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ContentLogoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
