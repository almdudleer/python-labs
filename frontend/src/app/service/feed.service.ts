import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Feed} from "../model/feed";
import {environment} from "../../environments/environment";
import {Entry} from "../model/entry";

@Injectable({
  providedIn: 'root'
})
export class FeedService {

  private url = `${environment.url}/feed`

  constructor(private http: HttpClient) {
  }

  public getFeeds(): Observable<Feed[]> {
    return this.http.get<Feed[]>(this.url);
  }

  public getFeed(feedId: string): Observable<Feed> {
    return this.http.get<Feed>(`${this.url}/${feedId}`);
  }

  public getFeedEntries(feedId: string, fromDate: string = ''): Observable<Entry[]> {
    if (fromDate) {
      fromDate = '?fromDate=' + fromDate.replace('+', '%2b');
    }
    return this.http.get<Entry[]>(`${this.url}/${feedId}/entries${fromDate}`);
  }

  public addFeed(feedUrl: string): Observable<any> {
    return this.http.post<any>(this.url, {feedUrl})
  }

  public updateFeed(feedId: string): Observable<any> {
    return this.http.patch<any>(this.url, {feedId})
  }
}
