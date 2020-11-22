import {Entry} from "./entry";

export class Feed {
  _id: string;
  title: string;
  href: string;
  image: string;
  entries?: Entry[];
}
