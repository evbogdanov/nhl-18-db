import { Injectable } from '@angular/core';
import { Skater } from './skater.model';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';


export interface SkatersPagination {
  start: number;
  end: number;
  per_page: number;
  pages: number;
  page: number;
}


export interface SkatersResponse {
  skaters: Skater[];
  pagination: SkatersPagination;
}


@Injectable()
export class SkaterService {
  private skatersUrl = '/api/skaters/';

  constructor(private http: HttpClient) {}

  searchSkaters(query): Observable<SkatersResponse> {
    let params = new HttpParams();
    for (const key of Object.keys(query)) {
      if (query[key] !== null && query[key] !== 'null') {
        params = params.append(key, query[key]);
      }
    }
    return this.http.get<SkatersResponse>(this.skatersUrl, {params});
  }

  getSkater(nhlcom_id): Observable<Skater|null> {
    return this.http.get<Skater|null>(`${this.skatersUrl}${nhlcom_id}/`);
  }
}
