import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { LocalStorageService } from "./localStorageService.service";


@Injectable({ providedIn: 'root' })
export class AuthServce {
    private apiRoot = 'http://localhost:8000/'
    constructor(private http: HttpClient, private authStorageService: LocalStorageService) {

    }

    signup(email: string, password: string) {
        const request_body = {
            "email": email,
            "password": password
        }
        this.http.post(this.apiRoot.concat('signup'), request_body).subscribe(data => {
            console.log(data)
        })
    }
    login(email: string, password: string) {
        const request_body = {
            "email": email,
            "password": password
        }
        this.http.post(this.apiRoot.concat('login'), request_body).subscribe(data => {
            console.log(data) // token comes here 
            var recievedToken = JSON.parse(JSON.stringify(data))  // parsing the token in json
            //console.log(recievedToken['token'])   // to retrieve the token
            this.authStorageService.set('token', recievedToken['token'])   // setting the token to local storage
            console.log(this.authStorageService.get('token'))  // getting the local storage service 
        })
    }
    logout() {
        localStorage.removeItem('token')
    }
}