import re

from array_stack import ArrayStack, EmptyStackError
from binary_tree import BinaryTree


def parse_expression(tokens):
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = ArrayStack()
    for token in tokens:
        try:
            token = BinaryTree(int(token))
        except ValueError:
            pass
        if token not in parentheses:
            stack.push(token)
        else:
            try:
                arg_2 = stack.pop()                # get arg2 if it has one
                operator = stack.pop()             # get the opertator if it has one
                arg_1 = stack.pop()                # get arg1 if it has oen
                opening_group_symbol = stack.pop() # get the operate symble
                if parentheses[token] != opening_group_symbol:
                    return
                parse_tree = BinaryTree(operator) # initialize a tree
                parse_tree.left_node = arg_1      # initialize a left  node of a tree
                parse_tree.right_node = arg_2     # initialize a right node of a tree
                stack.push(parse_tree)            # push it to stack
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    parse_tree = stack.pop()
    if not stack.is_empty():
        return
    return parse_tree


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
    parse_tree('{(1 + 20)*(30 - 400)}').print_binary_tree()
