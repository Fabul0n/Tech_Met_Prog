import json
from datetime import datetime
import typing_extensions

def serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y.%m.%d')

@typing_extensions.deprecated()
def save_to_file(files: list, filename: str):
    with open(filename, 'w') as f:
        f.write(files)

def save_to_json(files: list, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([_.model_dump() for _ in files], f, default=serializer, ensure_ascii=False, indent=4)