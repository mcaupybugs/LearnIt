import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";


@Injectable({ providedIn: 'root' })
export class AuthServce {

    private apiRoot = 'http://localhost:8000/'
    constructor(private http: HttpClient) {

    }

    signup(email: string, password: string) {
        const request_body = {
            "email": email,
            "password": password
        }
        const responserecieved = this.http.post(this.apiRoot.concat('signup'), request_body).subscribe(data => {
            console.log(data)
        })
        console.log(responserecieved)
    }
}