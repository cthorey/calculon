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

    Stop when the expression is only 1 character. 

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
    """calculate infix expression

    This solution use recursion:

    1. Find the inner computation ( a + b )
    2. As soon as you found one, compute the result
    3. Replace the computation by its result in the expression
    4. Apply calculate_infix to the resulting expression

    Stop when the expression is only 1 character.

    Args:
        expresion (str): Input infix expression

    Returns:
        result (int)
    """
    tokens = expression.split(' ')
    current = []
    for token in tokens:
        if token == "(":
            current = []
            continue
        if token == ")":
            a, ops, b = current
            result = OPS[ops](int(a), int(b))
            token = "( {} )".format(' '.join(current))
            expression = expression.replace(token, str(result))
            return calculate_infix(expression)
        current.append(token)
    return int(expression)
