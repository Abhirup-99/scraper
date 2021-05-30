from html.parser import HTMLParser
from typing import Set
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self, base_url: str, page_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links: Set[str] = set()

    def page_links(self) -> Set[str]:
        return self.links
