import operator

# operand mapping
OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculate_prefix(expression: str) -> int:
    """calculate prefix expression.

    This solution use recursion:
    1. Read the expression from the end
    2. As soon as you find an operator
    3. Apply it to the next two parameters
    4. Passe the resulting expression to calculate_prefix.

    Args:
        expresion (str): Input prefix expression

    Returns:
        result (int)
    """
    tokens = expression.split(' ')
    if len(tokens) == 1:
        return int(tokens[0])
    current_operation = []
    while tokens:
        current_operation.append(tokens.pop())
        if current_operation[-1] not in OPS.keys():
            continue
        current_operation = current_operation[::-1]
        ops, a, b = current_operation[:3]
        result = OPS[ops](int(a), int(b))
        expression = ' '.join(tokens + [str(result)] + current_operation[3:])
        return calculate_prefix(expression)


def calculate_infix(expression: str) -> int:
    return 0
