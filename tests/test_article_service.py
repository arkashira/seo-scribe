import pytest
from src.article import Article
from src.article_repository import ArticleRepository
from src.article_service import ArticleService

def test_article_service_save_article():
    service = ArticleService()
    article = Article(1, "Title", "Content", [])
    service.save_article(article)
    assert service.repository.articles == {1: article}

def test_article_service_get_article():
    service = ArticleService()
    article = Article(1, "Title", "Content", [])
    service.save_article(article)
    assert service.get_article(1) == article
