import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {FeedService} from "../service/feed.service";
import {Feed} from "../model/feed";
import {mergeMap} from "rxjs/operators";

@Component({
  selector: 'app-rss-reader',
  templateUrl: './rss-reader.component.html',
  styleUrls: ['./rss-reader.component.less'],
  encapsulation: ViewEncapsulation.None
})
export class RssReaderComponent implements OnInit {

  allFeeds: Feed[];

  feeds: Feed[];
  searchString = "";
  rssUrl = "";
  defaultImage = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Generic_Feed-icon.svg/120px-Generic_Feed-icon.svg.png";

  constructor(private feedService: FeedService) {
  }

  ngOnInit(): void {
    this.feedService.getFeeds().subscribe(feeds => {
      this.allFeeds = feeds;
      this.feeds = [...this.allFeeds];
    });
  }

  search(): void {
    this.feeds = this.allFeeds.filter(feed => feed.title.toLowerCase().includes(this.searchString.toLowerCase()))
  }

  addNewFeed(): void {
    this.feedService.addFeed(this.rssUrl).pipe(
      mergeMap(_ => this.feedService.getFeeds())
    ).subscribe(feeds => {
      this.allFeeds = feeds;
      this.feeds = [...this.allFeeds];
    });
    this.rssUrl = "";
  }

  fallbackToDefaultImage(event: ErrorEvent) {
    (<HTMLImageElement>event.target).src = this.defaultImage;
  }
}
