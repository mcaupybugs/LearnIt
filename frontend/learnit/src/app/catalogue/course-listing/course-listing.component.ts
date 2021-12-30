import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { LocalStorageService } from 'src/app/login/localStorageService.service';
import { Course } from 'src/app/model';

@Component({
  selector: 'app-course-listing',
  templateUrl: './course-listing.component.html',
  styleUrls: ['./course-listing.component.css']
})
export class CourseListingComponent implements OnInit {
  @Input('course') course!: Course;
  @Input('isBought') isBought!: Boolean;
  isLoggedIn!: Boolean
  private apiRoot = 'http://localhost:8000/'

  constructor(private storageService: LocalStorageService, private http: HttpClient) { }
  buyCourse() {
    var token = this.storageService.get('token');
    var headers_object = new HttpHeaders().set("Authorization", "Bearer " + token);
    const httpOptions = {
      headers: headers_object
    }
    var targetString = this.apiRoot.concat('buycourse/');
    targetString = targetString.concat(this.course.course_id);
    this.http.get(targetString, httpOptions).subscribe(data => {
      console.log(data) // gets the course. need to make the function to add the course first
    })
  }
  ngOnInit(): void {
    var token = this.storageService.get('token')
    if (token == null || this.isBought == true) {
      this.isLoggedIn = false;
    } else {
      this.isLoggedIn = true
    }
  }
}
