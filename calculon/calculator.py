import operator

# operand mapping
OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculate_prefix(expression: str) -> int:
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
