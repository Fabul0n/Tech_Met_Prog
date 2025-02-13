from datetime import datetime
from pydantic import BaseModel
from schemas.custom_file import CustomFile as CustomFileSchema
from schemas.mp4_file import Mp4File as Mp4FileSchema
from schemas.txt_file import TxtFile as TxtFileSchema
from abc import abstractmethod



class CustomFile[T: BaseModel](BaseModel):
    def __init__(self):
        self.name: str | None = None
        self.creation_date: datetime | None = None
        self.size: int | None = None

    
class TxtFile(CustomFile[TxtFileSchema]):
    def __init__(self, lines_count, words_count):
        super().__init__()
        self.lines_count = lines_count,
        self.words_count = words_count

    def from_dict(self, source: TxtFileSchema) -> None:
        self.name = source.name
        self.creation_date = source.creation_date
        self.size = source.size
        self.lines_count = source.lines_count
        self.words_count = source.words_count

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "creation_date": self.creation_date,
            "size": self.size,
            "lines_count": self.lines_count,
            "words_count": self.words_count
        }


class MP4File(CustomFile[Mp4FileSchema]):
    def __init__(self, duration, resolution):
        super().__init__()
        self.duration: int = duration
        self.resolution: int = resolution

    def from_dict(self, source: Mp4FileSchema) -> None:
        self.name = source.name
        self.creation_date = source.creation_date
        self.size = source.size
        self.duration = source.duration
        self.resolution = source.resolution