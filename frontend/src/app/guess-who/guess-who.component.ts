import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {Task} from '../model/task';
import {GuessService} from "../service/guess.service";

@Component({
  selector: 'app-guess-who',
  templateUrl: './guess-who.component.html',
  styleUrls: ['./guess-who.component.less'],
  encapsulation: ViewEncapsulation.None
})
export class GuessWhoComponent implements OnInit {
  step = 0;
  task: Task;
  result = '';

  constructor(private guessService: GuessService) {
  }

  ngOnInit(): void {
  }

  newGame(): void {
    this.step = 1;
    this.result = '';
    this.task = null;
    this.guessService.getTask().subscribe(task => {
      this.task = task;
    })
  }

  answer(name: string): void {
    this.step = 2;
    this.guessService.checkAnswer(this.task.id, name).subscribe(res => {
      this.result = res ? 'Всё верно!' : 'Вы ошиблись!';
    }, err => {
      this.result = 'Время вышло!'
    })
  }
}
