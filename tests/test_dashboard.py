from dashboard import Dashboard, Article
from datetime import datetime

def test_add_article():
    dashboard = Dashboard()
    article = Article(
        title="Test Article",
        description="Test description",
        keywords=["test", "seo"],
        date=datetime(2023, 1, 1)
    )
    dashboard.add_article(article)
    assert len(dashboard.articles) == 1
    assert dashboard.articles[0].title == "Test Article"

def test_filter_by_keyword():
    dashboard = Dashboard()
    article1 = Article(
        title="SEO Basics",
        description="Introduction to SEO",
        keywords=["seo", "basics"],
        date=datetime(2023, 1, 1)
    )
    article2 = Article(
        title="Advanced SEO",
        description="Advanced techniques",
        keywords=["seo", "advanced"],
        date=datetime(2023, 1, 2)
    )
    dashboard.add_article(article1)
    dashboard.add_article(article2)
    
    results = dashboard.filter_by_keyword("advanced")
    assert len(results) == 1
    assert results[0].title == "Advanced SEO"

def test_filter_by_date():
    dashboard = Dashboard()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 2)
    article1 = Article(
        title="Test 1",
        description="First test",
        keywords=["test"],
        date=date1
    )
    article2 = Article(
        title="Test 2",
        description="Second test",
        keywords=["test"],
        date=date2
    )
    dashboard.add_article(article1)
    dashboard.add_article(article2)
    
    results = dashboard.filter_by_date(date1)
    assert len(results) == 1
    assert results[0].title == "Test 1"

def test_sort_by_title():
    dashboard = Dashboard()
    article1 = Article(
        title="Zebra",
        description="Last in order",
        keywords=["animals"],
        date=datetime(2023, 1, 1)
    )
    article2 = Article(
        title="Apple",
        description="First in order",
        keywords=["fruits"],
        date=datetime(2023, 1, 2)
    )
    dashboard.add_article(article1)
    dashboard.add_article(article2)
    
    sorted_articles = dashboard.sort_by_title()
    assert sorted_articles[0].title == "Apple"
    assert sorted_articles[1].title == "Zebra"

def test_sort_by_date():
    dashboard = Dashboard()
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 2)
    article1 = Article(
        title="Old Article",
        description="First date",
        keywords=["history"],
        date=date1
    )
    article2 = Article(
        title="New Article",
        description="Second date",
        keywords=["future"],
        date=date2
    )
    dashboard.add_article(article1)
    dashboard.add_article(article2)
    
    sorted_articles = dashboard.sort_by_date()
    assert sorted_articles[0].title == "Old Article"
    assert sorted_articles[1].title == "New Article"
    
    reverse_sorted = dashboard.sort_by_date(reverse=True)
    assert reverse_sorted[0].title == "New Article"
    assert reverse_sorted[1].title == "Old Article"
