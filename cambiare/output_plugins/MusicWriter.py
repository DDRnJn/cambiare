from abc import ABC, abstractmethod
from core import Song


class MusicWriter(ABC):

    @abstractmethod
    def process_output(self, song: Song, filename: str):
        pass
