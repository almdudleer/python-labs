import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {RssReaderComponent} from "./rss-reader/rss-reader.component";
import {RssChooseFeedComponent} from "./rss-reader/rss-choose-feed/rss-choose-feed.component";
import {RssFeedComponent} from "./rss-reader/rss-feed/rss-feed.component";
import {GuessWhoComponent} from "./guess-who/guess-who.component";

const routes: Routes = [{
  path: '',
  pathMatch: 'full',
  redirectTo: '/rss'
}, {
  path: 'rss',
  component: RssReaderComponent,
  children: [
    {path: '', component: RssChooseFeedComponent},
    {path: ':feedId', component: RssFeedComponent}
  ]
}, {
  path: 'quiz',
  component: GuessWhoComponent
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
