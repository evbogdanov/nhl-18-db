import { Component } from '@angular/core';
import { Suggestion } from '../suggestions/suggestion.model';
import { SuggestionService } from '../suggestions/suggestion.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  suggestions: Suggestion[] = [];

  constructor(
    private router: Router,
    private suggestionService: SuggestionService
  ) { }
  
  getSuggestions(name) {
    if (name === '') {
      this.suggestions = [];
    }
    else {
      this.suggestionService.getSuggestions(name)
        .subscribe(suggestions => this.suggestions = suggestions)
    }
  }
  
  clearSuggestionsAndNavigate(input, destination) {
    input.value = '';
    this.suggestions = [];
    this.router.navigate(destination);
  }
  
}
