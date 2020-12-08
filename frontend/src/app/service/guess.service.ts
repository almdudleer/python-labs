import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Task} from '../model/task';
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class GuessService {

  private url = `${environment.url}/guess`

  constructor(private http: HttpClient) {
  }

  public getTask(optionsCount: number): Observable<Task> {
    return this.http.get<Task>(`${this.url}?optionsCount=${optionsCount}`);
  }

  public checkAnswer(taskId: string, answer: string): Observable<any> {
    return this.http.post<any>(this.url, {taskId, answer});
  }
}
