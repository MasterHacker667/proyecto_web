import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegistroService {
  private apiUrl = 'http://localhost:8080/loguser/';
  constructor(private http: HttpClient) {}

  public registrarUsuario(usuario: any): Observable<any> {
    const url = "http://localhost:8080/loguser/"
    return this.http.post(url, usuario);
  }
}