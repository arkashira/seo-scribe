from seo_scribe import SeoScribe, Brand, Keyword, Article
import json
import io
import sys

def test_generate_article():
    brand = Brand("Example Brand", "This is an example brand")
    keywords = [Keyword("SEO", 10), Keyword("Content Generation", 5)]
    seo_scribe = SeoScribe(brand, keywords)
    article = seo_scribe.generate_article()
    assert article.title.startswith(brand.name)
    assert any(keyword.word in article.content for keyword in keywords)

def test_generate_content():
    brand = Brand("Example Brand", "This is an example brand")
    keywords = [Keyword("SEO", 10), Keyword("Content Generation", 5)]
    seo_scribe = SeoScribe(brand, keywords)
    article = seo_scribe.generate_article()
    content = article.content
    assert len(content.split("\n\n")) == 5

def test_generate_paragraph():
    brand = Brand("Example Brand", "This is an example brand")
    keywords = [Keyword("SEO", 10), Keyword("Content Generation", 5)]
    seo_scribe = SeoScribe(brand, keywords)
    article = seo_scribe.generate_article()
    content = article.content
    paragraphs = content.split("\n\n")
    for paragraph in paragraphs:
        sentences = paragraph.split(". ")
        assert len(sentences) == 3

def test_main():
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    brand = Brand("Example Brand", "This is an example brand")
    keywords = [Keyword("SEO", 10), Keyword("Content Generation", 5)]
    seo_scribe = SeoScribe(brand, keywords)
    seo_scribe.print_article()
    sys.stdout = sys.__stdout__
    output = capturedOutput.getvalue()
    assert "title" in output
    assert "content" in output
