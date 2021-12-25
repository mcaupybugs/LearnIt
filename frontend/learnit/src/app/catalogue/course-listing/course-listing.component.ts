import { Component, Input, OnInit } from '@angular/core';
import { Course } from 'src/app/model';

@Component({
  selector: 'app-course-listing',
  templateUrl: './course-listing.component.html',
  styleUrls: ['./course-listing.component.css']
})
export class CourseListingComponent implements OnInit {
  @Input('course') course!: Course;
  constructor() { }

  ngOnInit(): void {
  }
}
