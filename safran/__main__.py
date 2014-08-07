# -*- coding: utf-8 -*-

import feedparser
from clint.textui import colored, puts, indent


def main():
    feeds = feedparser.parse('http://www.safran.io/feed.rss')
    for entry in feeds["entries"][0:10]:
        with indent(2):
            puts("\n\xF0\x9F\x94\xB9 {0}\n\t{1}".format(
                colored.magenta(entry["title"].encode("utf-8"), bold=True),
                entry["link"])
            )


if __name__ == '__main__':
    main()