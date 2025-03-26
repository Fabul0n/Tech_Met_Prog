import json
from datetime import datetime
from .logger import error_logger as logger

def serializer(obj):
    try:
        if isinstance(obj, datetime):
            return obj.strftime('%Y.%m.%d')
    except Exception as e:
        logger.error(f'Datetime serializer error. Value: {obj}')

def save_to_file(files: list, filename: str):
    try:
        with open(filename, 'w') as f:
            f.write(files)
    except Exception as e:
        logger.error(f'Error while saving to file: {str(e)}')

def save_to_json(files: list, filename: str):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({f'file{i}':file.model_dump() for i, file in enumerate(files)}, f, default=serializer, ensure_ascii=False, indent=4)
    except Exception as e:
        logger.error(f'Error while saving to json file: {str(e)}')
