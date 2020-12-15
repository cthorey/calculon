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

    This solution uses a stack

    Args:
        expresion (str): Input prefix expression

    Returns:
        result (int)
    """
    stack = []
    tokens = expression.split(' ')
    for token in tokens[::-1]:
        if token not in OPS.keys():
            stack.append(token)
            continue
        a = stack.pop()
        b = stack.pop()
        result = OPS[token](int(a), int(b))
        stack.append(result)
    return int(stack.pop())


def calculate_infix(expression: str) -> int:
    """calculate infix expression

    Args:
        expresion (str): Input infix expression

    Returns:
        result (int)
    """
    stack = []
    tokens = expression.split(' ')
    for token in tokens:
        if token == '(':
            continue
        if token != ')':
            stack.append(token)
            continue
        b = stack.pop()
        ops = stack.pop()
        a = stack.pop()
        result = OPS[ops](int(a), int(b))
        stack.append(result)
    return int(stack.pop())
