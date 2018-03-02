import { Country } from '../countries/country.model';

export interface Team {
  readonly abbrev: string;
  readonly name: string;
  readonly country: Country;
  readonly conference: string;
  readonly division: string;
  readonly is_active: boolean;
  readonly img: string;
}
