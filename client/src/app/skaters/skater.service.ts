import { Injectable } from '@angular/core';
import { Skater } from './skater.model';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';


@Injectable()
export class SkaterService {
  private skatersUrl = '/api/skaters/';

  constructor(private http: HttpClient) {}

  searchSkaters(query): Observable<Skater[]> {
    let params = new HttpParams();
    for (const key of Object.keys(query)) {
      if (query[key] !== null && query[key] !== 'null') {
        params = params.append(key, query[key]);
      }
    }
    return this.http.get<Skater[]>(this.skatersUrl, {params});
  }
}
