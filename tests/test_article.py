import pytest
from src.article import Article

def test_article_creation():
    article = Article(1, "Title", "Content", [])
    assert article.id == 1
    assert article.title == "Title"
    assert article.content == "Content"
    assert article.versions == []

def test_article_add_version():
    article = Article(1, "Title", "Content", [])
    article.add_version("Version 1")
    assert article.versions == ["Version 1"]

def test_article_get_latest_version():
    article = Article(1, "Title", "Content", ["Version 1", "Version 2"])
    assert article.get_latest_version() == "Version 2"
