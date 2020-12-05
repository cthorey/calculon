from calculon import calculator

MSG = """

#########################################
Running {name} test
########################################

"""

# prefix test cases
PREFIX = {
    '3': 3,
    '+ 1 2': 3,
    '+ 1 * 2 3': 7,
    '- / 10 + 1 1 * 1 2': 3,
    '- 0 3': -3,
    '/ 3 2': 1,
    '- + 1 2 + * 3 2 5': -8
}

# infix test cases
INFIX = {
    '( 1 + 2 )': 3,
    '( 1 + ( 2 * 3 ) )': 7,
    '( ( 1 * 2 ) + 3 )': 5,
    '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )': -2
}


def test_prefix_calculator():
    print(MSG.format(name='prefix calculator'))
    # loop through the test-cases and make sure they pass
    for expression, value in PREFIX.items():
        print('Checking {} : {}'.format(expression, value))
        result = calculator.calculate_prefix(expression)
        assert result == value, "Fail on \"{}\". Expected :{} / Returned: {}".format(
            expression, value, result)
    print('Sucessfully ran prefix test \n')


def test_infix_calculator():
    print(MSG.format(name='infix calculator'))
    for expression, value in INFIX.items():
        print('Checking {} : {}'.format(expression, value))
        result = calculator.calculate_infix(expression)
        assert result == value, "Fail on \"{}\". Expected :{} / Returned: {}".format(
            expression, value, result)
    print('Sucessfully ran infix test  \n')
