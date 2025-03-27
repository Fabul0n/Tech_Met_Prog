from datetime import datetime

def return_date_sum(date: str):
    try:
        dt = datetime.strptime(date, '%d.%m.%Y')
        return sum(map(int, list(dt.strftime('%d%m%Y'))))
    except Exception as e:
        return None

def test_date_sum():
    res = [return_date_sum("12.12.2000"), return_date_sum("123.123.123"), return_date_sum("16.12.2000")]
    exp = [8, None, 12]
    for i in range(len(res)):
        assert res[i] == exp[i]
