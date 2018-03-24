import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'shortPosition'
})
export class ShortPositionPipe implements PipeTransform {

  transform(position: any, args?: any): any {
    switch(position) {
    case 'Center':
      return 'C';
    case 'Left Wing':
      return 'LW';
    case 'Right Wing':
      return 'RW';
    case 'Defenseman':
      return 'D';
    default:
      return position;
    }
  }

}
