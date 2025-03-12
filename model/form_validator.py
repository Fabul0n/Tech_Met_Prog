from enum import Enum

class Fields(Enum):
    name = 'Название файла'
    creation_date = 'Дата создания'
    size = 'Размер'
    words_count = 'Количество слов'
    lines_count = 'Количество строк'
    duration = 'Длительность'
    resolution = 'Разрешение'

def validate_data(data: dict):
    for key, value in data.items():
        if not value:
            return False, f"Поле '{Fields[key].value}' не может быть пустым."
    return True, ""