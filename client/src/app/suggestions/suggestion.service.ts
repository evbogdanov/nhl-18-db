import { Injectable } from '@angular/core';
import { Suggestion } from './suggestion.model';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';


@Injectable()
export class SuggestionService {
  private suggestionsUrl = '/api/suggestions/';

  constructor(private http: HttpClient) {}

  getSuggestions(name): Observable<Suggestion[]> {
    const params = new HttpParams().set('name', name);
    return this.http.get<Suggestion[]>(this.suggestionsUrl, {params});
  }

}
