import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Router } from "@angular/router";
import { LocalStorageService } from "./localStorageService.service";


@Injectable({ providedIn: 'root' })
export class AuthServce {
    private apiRoot = 'http://localhost:8000/'
    constructor(private http: HttpClient, private authStorageService: LocalStorageService, private router: Router) {

    }

    signup(email: string, password: string) {
        const request_body = {
            "email": email,
            "password": password
        }
        this.http.post(this.apiRoot.concat('signup'), request_body, { responseType: 'text' }).subscribe(data => {
            console.log("Running")
            this.router.navigate(['/'])
        }, error => {
            console.log("Error")
            console.log(error);
        })
    }
    login(email: string, password: string) {
        const request_body = {
            "email": email,
            "password": password
        }
        this.http.post(this.apiRoot.concat('login'), request_body).subscribe(data => {
            console.log("printing data")
            console.log(data) // token comes here 
            var recievedToken = JSON.parse(JSON.stringify(data))  // parsing the token in json
            //console.log(recievedToken['token'])   // to retrieve the token
            this.authStorageService.set('token', recievedToken['token'])   // setting the token to local storage
            console.log(this.authStorageService.get('token'))  // getting the local storage service 

            this.router.navigate(['/'])
        }, error => {
            console.log(error)
        })
    }
    logout() {
        localStorage.removeItem('token')
    }
}