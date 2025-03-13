from datetime import datetime
from pydantic import BaseModel, field_validator, ValidationError, ConfigDict


class CustomFile(BaseModel):
    name: str
    creation_date: datetime
    size: int

    @field_validator('creation_date', mode='before')
    def check_date(cls, value: str):
        return datetime.strptime(value, '%Y.%m.%d')
    
    @property
    def formated_creation_date(self) -> str:
        return self.__dict__.get('creation_date').strftime('%Y.%m.%d')

    model_config = ConfigDict(extra='forbid', json_encoders={datetime: lambda dt: dt.strftime('%Y.%m.%d')})

    
class TxtFile(CustomFile):
    lines_count: int
    words_count: int


class MP4File(CustomFile):
    duration: int
    resolution: str

    @field_validator('resolution')
    def check_resolution(cls, value: str):
        ls = value.split('x')
        try:
            if len(ls) == 2 and int(ls[0]) == float(ls[0]) and int(ls[1]) == float(ls[1]):
                return value
        except Exception:
            e = ValidationError()
            e.add_note("Resolution must have <int>x<int> format")
            raise e