import { Component, Input, OnInit } from '@angular/core';
import { Course } from '../model';

@Component({
  selector: 'app-catalogue',
  templateUrl: './catalogue.component.html',
  styleUrls: ['./catalogue.component.css']
})
export class CatalogueComponent implements OnInit {

  @Input('catalogue') catalogueCourses!: Course[];
  @Input('catalogue-title') catalogueTitle!: String;
  @Input('catalogue-text') catalogueText!: String;
  @Input('isBought') isBought!: Boolean;
  constructor() { }

  ngOnInit(): void {
  }

}
