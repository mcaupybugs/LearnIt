import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LocalStorageService } from '../login/localStorageService.service';
import { Course } from '../model';

@Component({
  selector: 'app-my-courses',
  templateUrl: './my-courses.component.html',
  styleUrls: ['./my-courses.component.css']
})
export class MyCoursesComponent implements OnInit {
  private apiRoot = 'http://localhost:8000/'

  constructor(private storageService: LocalStorageService, private router: Router, private http: HttpClient) { }
  courses!: Course[]
  isBought = true;
  catalogueTitle = "Your Catalogue"
  catalogueText = "All the courses bought by you !!"
  getCourse() {

    var token = this.storageService.get('token');
    if (token == null) {
      this.router.navigate(['/login'])
    }
    var headers_object = new HttpHeaders().set("Authorization", "Bearer " + token);
    const httpOptions = {
      headers: headers_object
    }
    this.http.get(this.apiRoot.concat('mycourse'), httpOptions).subscribe(data => {
      var parsedData = JSON.parse(JSON.stringify(data))
      this.courses = parsedData
      console.log(this.courses)

    })
  }
  ngOnInit(): void {
    this.getCourse()
  }

}
