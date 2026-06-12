from src.article import Article

class ArticleRepository:
    def __init__(self):
        self.articles = {}

    def save_article(self, article: Article):
        self.articles[article.id] = article

    def get_article(self, id: int):
        return self.articles.get(id)
