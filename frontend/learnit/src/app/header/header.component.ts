import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { AuthServce } from '../login/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  isLoggedIn = false;
  constructor(private authService: AuthServce) { }

  ngOnInit(): void {
    var token = localStorage.getItem('token')
    console.log("token")
    console.log(token)
    if (token == null) {
      this.isLoggedIn = false;
    } else {
      this.isLoggedIn = true;
    }
  }

  logout() {
    this.authService.logout();
    this.ngOnInit();
  }

}
