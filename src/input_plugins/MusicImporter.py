from abc import ABC, abstractmethod
from src.core import Song


class MusicImporter(ABC):

    @abstractmethod
    def process_input(self, contents) -> Song:
        pass
