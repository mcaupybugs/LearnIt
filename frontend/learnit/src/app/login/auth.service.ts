import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";


@Injectable({ providedIn: 'root' })
export class AuthServce {

    constructor(private http: HttpClient) {

    }

    signup(email: string, password: string) {
        return this.http.post('//urrl', null)
    }
}