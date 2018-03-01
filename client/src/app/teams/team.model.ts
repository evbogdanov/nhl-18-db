import { Country } from '../countries/country.model';

export class Team {
  constructor(readonly abbrev: string,
              readonly name: string,
              readonly country: Country,
              readonly conference: string,
              readonly division: string,
              readonly is_active: boolean = true) {}

  get img(): string {
    return `/static/img/team/${this.abbrev}.svg`
  }
}
