from src.article import Article
from src.article_repository import ArticleRepository

class ArticleService:
    def __init__(self):
        self.repository = ArticleRepository()

    def save_article(self, article: Article):
        self.repository.save_article(article)

    def get_article(self, id: int):
        return self.repository.get_article(id)
