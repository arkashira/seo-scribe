import pytest
from src.article import Article
from src.article_repository import ArticleRepository

def test_article_repository_save_article():
    repository = ArticleRepository()
    article = Article(1, "Title", "Content", [])
    repository.save_article(article)
    assert repository.articles == {1: article}

def test_article_repository_get_article():
    repository = ArticleRepository()
    article = Article(1, "Title", "Content", [])
    repository.save_article(article)
    assert repository.get_article(1) == article
