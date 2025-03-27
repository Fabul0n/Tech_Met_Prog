from model.form_validator import validate_data

'''
class Fields(Enum):
    name = 'Название файла'
    creation_date = 'Дата создания'
    size = 'Размер'
    words_count = 'Количество слов'
    lines_count = 'Количество строк'
    duration = 'Длительность'
    resolution = 'Разрешение'
'''

def test_validate_data():
    test_data = [
        {"name": "asd", "creation_date": "asd", "size": 123, "words_count": 123, "lines_count": 123, "duration": 123, "resolution": "123x123"}
    ]
    expected = [True]
    for i, d in enumerate(test_data):
        assert expected[i] == validate_data(d)[0]
