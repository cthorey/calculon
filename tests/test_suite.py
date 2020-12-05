import pytest
import requests
import json
from calculon import calculator
import yaml

with open('/config.yaml', 'r') as f:
    CONFIG = yaml.load(f, yaml.Loader)['api']

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


@pytest.mark.library
def test_prefix_calculator():
    # loop through the test-cases and make sure they pass
    for expression, value in PREFIX.items():
        result = calculator.calculate_prefix(expression)
        assert result == value, f"Fail on {expression}. Expected :{value} - returned: {result}"


@pytest.mark.library
def test_infix_calculator():
    for expression, value in INFIX.items():
        result = calculator.calculate_infix(expression)
        assert result == value, f"Fail on {expression}. Expected :{value} - returned: {result}"


@pytest.mark.api
def test_calculate_infix():
    for expression, result in INFIX.items():
        url = f"http://{CONFIG['host']}:{CONFIG['port']}/calculate_infix/"
        payload = dict(expression=expression)
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert json.loads(response.content)['result'] == result


@pytest.mark.api
def test_calculate_prefix():
    for expression, result in INFIX.items():
        url = f"http://{CONFIG['host']}:{CONFIG['port']}/calculate_infix/"
        payload = dict(expression=expression)
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert json.loads(response.content)['result'] == result
