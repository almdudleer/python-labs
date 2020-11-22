import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {ClarityModule} from '@clr/angular';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {RssFeedComponent} from "./rss-reader/rss-feed/rss-feed.component";
import {RssChooseFeedComponent} from "./rss-reader/rss-choose-feed/rss-choose-feed.component";
import {RssReaderComponent} from "./rss-reader/rss-reader.component";
import {HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";
import {GuessWhoComponent} from './guess-who/guess-who.component';
import {CommonModule} from "@angular/common";

@NgModule({
  declarations: [
    AppComponent,
    RssFeedComponent,
    RssChooseFeedComponent,
    RssReaderComponent,
    GuessWhoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ClarityModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    CommonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
