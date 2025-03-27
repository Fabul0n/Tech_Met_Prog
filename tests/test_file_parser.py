from model.file_parser import parse_json
from model.file_models import *

def test_parse_json():
    res = parse_json('./tests/test_inputs/input1.json')
    expected = [
        CustomFile(name='habsd', creation_date="2024.04.12", size=12342), 
        TxtFile(name='kjasdasd', creation_date="2024.12.05", size=4123, lines_count=12, words_count=1200), 
        MP4File(name='ojnasd', creation_date="2024.05.12", size=4124, duration=412442, resolution='1280x720')
    ]
    assert res == expected