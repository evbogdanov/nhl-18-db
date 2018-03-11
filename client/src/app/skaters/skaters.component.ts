import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-skaters',
  templateUrl: './skaters.component.html',
  styleUrls: ['./skaters.component.css']
})
export class SkatersComponent implements OnInit {
  searchForm: FormGroup;

  ngOnInit() {
    this.searchForm = new FormGroup({
      name: new FormControl(null),
      age_from: new FormControl(null),
      age_to: new FormControl(null),
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
