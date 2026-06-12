from dataclasses import dataclass
from typing import List

@dataclass
class Article:
    id: int
    title: str
    content: str
    versions: List[str]

    def add_version(self, version: str):
        self.versions.append(version)

    def get_latest_version(self):
        return self.versions[-1]
