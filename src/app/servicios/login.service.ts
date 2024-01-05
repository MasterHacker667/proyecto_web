import { HttpClient, HttpParamsOptions } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private opcionesHttp = {
    headers : {'Content-Type': 'application/json' }
  }

  constructor(private http: HttpClient) {
  }

  public LoginUser(usuario: string, password: string): Observable<any> {
    var loginInfo = {
      username: usuario,
      password: password
    };
    return this.http.post("https://dummyjson.com/auth/login", JSON.stringify(loginInfo), this.opcionesHttp);
  }
  
}
