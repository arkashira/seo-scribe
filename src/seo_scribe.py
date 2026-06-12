import json
from dataclasses import dataclass
from typing import List
import random

@dataclass
class Keyword:
    word: str
    frequency: int

@dataclass
class Brand:
    name: str
    description: str

@dataclass
class Article:
    title: str
    content: str

class SeoScribe:
    def __init__(self, brand: Brand, keywords: List[Keyword]):
        self.brand = brand
        self.keywords = keywords

    def generate_article(self) -> Article:
        title = f"{self.brand.name}: {self.keywords[0].word} Expertise"
        content = self._generate_content()
        return Article(title, content)

    def _generate_content(self) -> str:
        paragraphs = []
        for _ in range(5):
            paragraph = self._generate_paragraph()
            paragraphs.append(paragraph)
        return "\n\n".join(paragraphs)

    def _generate_paragraph(self) -> str:
        sentences = []
        for _ in range(3):
            sentence = self._generate_sentence()
            sentences.append(sentence)
        return ". ".join(sentences)

    def _generate_sentence(self) -> str:
        keyword = random.choice(self.keywords)
        sentence = f"{self.brand.name} is a leading expert in {keyword.word} with {keyword.frequency} years of experience."
        return sentence

    def print_article(self):
        article = self.generate_article()
        print(json.dumps({"title": article.title, "content": article.content}, indent=4))

def main():
    brand = Brand("Example Brand", "This is an example brand")
    keywords = [Keyword("SEO", 10), Keyword("Content Generation", 5)]
    seo_scribe = SeoScribe(brand, keywords)
    seo_scribe.print_article()

if __name__ == "__main__":
    main()
