import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { FORM_FIELDS } from './skaters.form';

@Component({
  selector: 'app-skaters',
  templateUrl: './skaters.component.html',
  styleUrls: ['./skaters.component.css']
})
export class SkatersComponent implements OnInit {
  formFields = FORM_FIELDS;
  searchForm: FormGroup;

  constructor(private fb: FormBuilder) {}
  
  ngOnInit() {
    this.buildForm();
  }

  buildForm() {
    const formObject = {};
    this.formFields.forEach(field => formObject[field.name] = null);
    this.searchForm = this.fb.group(formObject);
  }

  onSubmit() {
    for (let field in this.searchForm.value) {
      console.log(`${field} => ${this.searchForm.value[field]}`);
    }
  }

  onReset() {
    this.searchForm.reset();
  }

}
