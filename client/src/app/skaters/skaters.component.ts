import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { FORM_FIELDS } from './skaters.form';
import { Skater } from './skater.model';
import { SkaterService, SkatersPagination } from './skater.service';


@Component({
  selector: 'app-skaters',
  templateUrl: './skaters.component.html',
  styleUrls: ['./skaters.component.css']
})
export class SkatersComponent implements OnInit {
  formFields = FORM_FIELDS;
  searchForm: FormGroup;
  isSearching: boolean = false;
  skaters: Skater[] = [];
  pagination: null | SkatersPagination;

  constructor(private fb: FormBuilder,
              private skaterService: SkaterService) {}

  ngOnInit() {
    this.buildForm();
    this.search({page: 0});
  }

  search(query) {
    this.isSearching = true;
    this.skaters = [];
    this.pagination = null;
    this.skaterService.searchSkaters(query)
      .subscribe(skatersResponse => {
        this.isSearching = false;
        this.skaters = skatersResponse.skaters;
        this.pagination = skatersResponse.pagination;
      });
  }

  buildForm() {
    const formObject = {};
    this.formFields.forEach(field => formObject[field.name] = null);
    this.searchForm = this.fb.group(formObject);
  }

  onReset() {
    this.searchForm.reset();
  }

  onSubmit() {
    const query = this.searchForm.value;
    query.page = 0;
    this.search(query);
  }

  gotoPage(page) {
    const query = this.searchForm.value;
    query.page = page;
    this.search(query);
  }

  get pagesAsArray() {
    if (this.pagination === null) {
      return []
    }
    return new Array(this.pagination.pages).fill(0);
  }

}
