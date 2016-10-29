import re
from operator import add, sub, mul, truediv
from array_stack import ArrayStack, EmptyStackError


# evaluate('{1 + [((20*30)-400) / 500]}')


def get_value(tokens):
    parentheses = {')': '(', ']': '[', '}': '{'}
    operate = {'+': add, '-': sub, '*': mul, '/': truediv}
    stack = ArrayStack()
    for token in tokens:
        # if token is an integer, then we convert it to an int
        try:               token = int(token)
        except ValueError: pass
        # if token is an integer, we push it to stack
        if token not in parentheses:
            stack.push(token)
        # else, we try to find the last 4 values in stack by checking stack._data
        else:
            try:
                arg_2                = stack.pop()
                operator             = stack.pop()
                arg_1                = stack.pop()
                opening_group_symbol = stack.pop()
                if parentheses[token] != opening_group_symbol: return
                stack.push(operate[operator](arg_1, arg_2))
            except EmptyStackError:
                return            
    if stack.is_empty(): return
    value = stack.pop()
    if not stack.is_empty(): return
    return value


def evaluate(expression):
    # check whether the input is good or not.
    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        print('Your input is bad.')
        return
    # Tokens can be natural numbers, (, ), [, ], {, }, +, -, *, and /
    #tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    tokens = re.compile('(\d+|\+|\-|\*|/|\(|\)|\[|\]|{|})').findall(expression)
    #print(tokens)
    try:
        value = get_value(tokens)
        return value
    except ZeroDivisionError:
        print('Divisor cannot be zero.')
        return

print(evaluate('{1 + [((20*30)-400) / 500]}'))
