import json
from datetime import datetime
from pydantic import ValidationError

from .file_models import CustomFile, TxtFile, MP4File


def parse_json(filename: str):
    ls: list[CustomFile] = []
    with open(filename, 'r') as f:
        json_str: dict = json.loads(f.read())
        for key, value in json_str.items():
            try:
                ls.append(MP4File(**value))
            except ValidationError as e:
                try:
                    ls.append(TxtFile(**value))
                except ValidationError as e:
                    try:
                        ls.append(CustomFile(**value))
                    except ValidationError as e:
                        print(value)
    print(ls)
    return ls