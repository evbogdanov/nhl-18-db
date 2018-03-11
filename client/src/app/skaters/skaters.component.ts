import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-skaters',
  templateUrl: './skaters.component.html',
  styleUrls: ['./skaters.component.css']
})
export class SkatersComponent implements OnInit {
  searchForm: FormGroup;

  constructor(private fb: FormBuilder) {}
  
  ngOnInit() {
    this.searchForm = this.fb.group({
      name: null,
      age_from: null,
      age_to: null,
    });
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
