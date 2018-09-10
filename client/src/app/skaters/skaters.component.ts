import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { FORM_FIELDS } from './skaters.form';
import { Skater } from './skater.model';
import { SkaterService } from './skater.service';

@Component({
  selector: 'app-skaters',
  templateUrl: './skaters.component.html',
  styleUrls: ['./skaters.component.css']
})
export class SkatersComponent implements OnInit {
  formFields = FORM_FIELDS;
  searchForm: FormGroup;
  skaters: Skater[] = [];
  searched = false;

  constructor(private fb: FormBuilder,
              private skaterService: SkaterService) {}
  
  ngOnInit() {
    this.buildForm();
    this.searchAndUpdateSkaters();
  }

  searchAndUpdateSkaters(query = {}) {
    this.skaterService.searchSkaters(query)
      .subscribe(skaters => this.skaters = skaters);
  }

  buildForm() {
    const formObject = {};
    this.formFields.forEach(field => formObject[field.name] = null);
    this.searchForm = this.fb.group(formObject);
  }

  onSubmit() {
    this.searched = true;
    const query = this.searchForm.value;
    this.searchAndUpdateSkaters(query);
  }

  onReset() {
    this.searchForm.reset();
  }

}
