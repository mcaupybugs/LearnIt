import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthServce } from './auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  loginMode = true;
  constructor(private authService: AuthServce) {
  }
  changeMode() {
    this.loginMode = !this.loginMode
  }
  ngOnInit() {
    this.loginForm = new FormGroup({
      'email': new FormControl(null),
      'password': new FormControl(null)
    });
  }
  onSubmit() {
    var email = this.loginForm.value['email']
    var password = this.loginForm.value['password']
    if (this.loginMode == true) {
      this.authService.login(email, password)
    } else {
      console.log(this.loginForm.value['email']);
      this.authService.signup(email, password)
    }
  }
}
