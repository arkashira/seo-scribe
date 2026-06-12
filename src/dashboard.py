from dataclasses import dataclass
from typing import List, Optional, Callable, Any
from datetime import datetime

@dataclass
class Article:
    title: str
    description: str
    keywords: List[str]
    date: datetime

class Dashboard:
    def __init__(self):
        self.articles: List[Article] = []

    def add_article(self, article: Article) -> None:
        self.articles.append(article)

    def filter_by_keyword(self, keyword: str) -> List[Article]:
        return [article for article in self.articles if keyword in article.keywords]

    def filter_by_date(self, target_date: datetime) -> List[Article]:
        return [article for article in self.articles if article.date.date() == target_date.date()]

    def sort_by_title(self) -> List[Article]:
        return sorted(self.articles, key=lambda article: article.title)

    def sort_by_date(self, reverse: bool = False) -> List[Article]:
        return sorted(self.articles, key=lambda article: article.date, reverse=reverse)
