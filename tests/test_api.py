import requests
import json

CONFIG = {'host': '172.17.0.2', 'port': 80}

# infix test cases
INFIX = {
    '( 1 + 2 )': 3,
    '( 1 + ( 2 * 3 ) )': 7,
    '( ( 1 * 2 ) + 3 )': 5,
    '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )': -2
}

# prefix test case
PREFIX = {
    '3': 3,
    '+ 1 2': 3,
    '+ 1 * 2 3': 7,
    '- / 10 + 1 1 * 1 2': 3,
    '- 0 3': -3,
    '/ 3 2': 1,
    '- + 1 2 + * 3 2 5': -8
}


def test_calculate_infix():
    for expression, result in INFIX.items():
        url = f"http://{CONFIG['host']}:{CONFIG['port']}/calculate_infix/"
        payload = dict(expression=expression)
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert json.loads(response.content)['result'] == result


def test_calculate_prefix():
    for expression, result in INFIX.items():
        url = f"http://{CONFIG['host']}:{CONFIG['port']}/calculate_infix/"
        payload = dict(expression=expression)
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert json.loads(response.content)['result'] == result
