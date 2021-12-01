from urllib.request import urlopen
from urllib.parse import urlparse

import re
import sys

LINK_REGEX = re.compile(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"')


class LinkCollector:
    def __init__(self, url):
        self.url = "" + urlparse(url).netloc
        self.collected_links = set()
        self.visited_links = set()

    def collect_links(self, path="/"):
        full_url = self.url + path
        self.visited_links.add(full_url)
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        links = {self.normalize_url(path, link) for link in links}
        self.collected_links = links.union(self.collected_links)
        unvisited_links = links.difference(self.visited_links)
        print(links, self.collected_links, unvisited_links)
        return links

    def normalize_url(self, path, link):
        if link.startswith("http://"):
            return link
        elif link.startswith("/"):
            return self.url + link
        else:
            return self.url + "/" + path.rpartition("/")[0] + link
