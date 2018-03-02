import { Player } from '../players/player.model';

export interface Skater extends Player {
  readonly position: string;
  readonly type: string;
  readonly shoots: string;

  readonly puck_skills: number;
  readonly senses: number;
  readonly shooting: number;
  readonly defense: number;
  readonly skating: number;
  readonly physical: number;

  readonly deking: number;
  readonly hand_eye: number;
  readonly passing: number;
  readonly puck_control: number;

  readonly discipline: number;
  readonly offensive_awareness: number;
  readonly poise: number;

  readonly slap_shot_accuracy: number;
  readonly slap_shot_power: number;
  readonly wrist_shot_accuracy: number;
  readonly wrist_shot_power: number;

  readonly defensive_awareness: number;
  readonly faceoffs: number;
  readonly shot_blocking: number;
  readonly stick_checking: number;

  readonly acceleration: number;
  readonly agility: number;
  readonly balance: number;
  readonly endurance: number;
  readonly speed: number;

  readonly aggressiveness: number;
  readonly body_checking: number;
  readonly durability: number;
  readonly fighting_skill: number;
  readonly strength: number;
}
