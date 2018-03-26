import { Component, Input } from '@angular/core';
import { Renderer2 } from '@angular/core';
import { Router } from '@angular/router';

import { Suggestion } from '../suggestions/suggestion.model';
import { SuggestionService } from '../suggestions/suggestion.service';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  @Input() shadow: any;
  suggestions: Suggestion[] = [];

  constructor(
    private renderer: Renderer2,
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

  activateSearching(nav) {
    this.renderer.addClass(nav, 'searching');
    this.renderer.addClass(this.shadow, 'main-shadow_activated');
  }

  deactivateSearching(nav) {
    this.renderer.removeClass(nav, 'searching');
    this.renderer.removeClass(this.shadow, 'main-shadow_activated');
    this.suggestions = [];
  }

}
