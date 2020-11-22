import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {FeedService} from "../../service/feed.service";
import {Entry} from "../../model/entry";
import {Feed} from "../../model/feed";
import {mergeMap} from "rxjs/operators";

@Component({
  selector: 'app-rss-feed',
  templateUrl: './rss-feed.component.html',
  styleUrls: ['./rss-feed.component.less'],
  encapsulation: ViewEncapsulation.None
})
export class RssFeedComponent implements OnInit {

  entries: Entry[];
  currentFeed: Feed;

  constructor(private route: ActivatedRoute,
              private feedService: FeedService) {
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.entries = [];
      this.feedService.getFeedEntries(params.feedId).subscribe(entries => {
        this.entries = entries
      });
    });
  }

  refresh(): void {
    this.feedService.updateFeed(this.route.snapshot.params.feedId).pipe(
      mergeMap(_ => {
        return this.feedService.getFeedEntries(this.route.snapshot.params.feedId);
      })
    ).subscribe(entries => {
      this.entries = entries
    });
  }

  loadNewPage(): void {
    const dateFrom = this.entries[this.entries.length - 1].published;
    this.feedService.getFeedEntries(this.route.snapshot.params.feedId, dateFrom).subscribe(entries => {
      this.entries = [...this.entries, ...entries];
    });
  }
}
