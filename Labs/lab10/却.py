import re

from array_stack import ArrayStack, EmptyStackError
from binary_tree import BinaryTree


def parse_expression(tokens):
    print(tokens)
    return 'wat'

def parse_tree(expression):
    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, (, ), [, ], {, }, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = parse_expression(tokens)
        return value
    except ZeroDivisionError:
        return

if __name__ == '__main__':
    parse_tree('{(1 + 20)*(30 - 400)}')#.print_binary_tree()
