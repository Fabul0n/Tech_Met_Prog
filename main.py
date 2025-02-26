from datetime import datetime
from pydantic import BaseModel, field_validator, ValidationError, ConfigDict
import json



class CustomFile(BaseModel):
    name: str
    creation_date: datetime
    size: int

    @field_validator('creation_date')
    def check_date(cls, value: datetime):
        return value.strftime('%Y.%m.%d')
    
    model_config = ConfigDict(extra='forbid')

    
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

def parse_json(filename: str):
    ls: list[CustomFile] = []
    with open(filename, 'r') as f:
        json_str: dict = json.loads(f.read())
        for key, value in json_str.items():
            try:
                ls.append(MP4File(**value))
            except ValidationError:
                try:
                    ls.append(TxtFile(**value))
                except ValidationError:
                    try:
                        ls.append(CustomFile(**value))
                    except ValidationError:
                        print(value)
    return ls
                


print(parse_json('example.json'))