import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Course } from '../model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  private apiRoot = 'http://localhost:8000/'
  constructor(private api: HttpClient) { }
  catalogueCourses!: Course[]
  getCatalogue() {  // check how to make tha application wait for res to return object
    this.api.get(this.apiRoot.concat('catalogue')).subscribe(data => {
      var recievedData = JSON.parse(JSON.stringify(data))
      this.catalogueCourses = recievedData
      console.log(this.catalogueCourses)
    })
  }
  ngOnInit(): void {
    this.getCatalogue(); // to get the list of all the courses at homepage 

  }

}
