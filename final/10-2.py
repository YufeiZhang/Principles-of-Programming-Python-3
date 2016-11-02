import re

from array_stack import ArrayStack, EmptyStackError
from binary_tree import BinaryTree

def parse_expression(tokens):
    end = {')': '(', ']': '[', '}': '{'}
    stack = ArrayStack()

    for t in tokens:
        try:
            t = BinaryTree(int(t)) # if it is a digit
        except ValueError:
            pass
        if t not in end:  # if it is not the end of any kind of bracket
            stack.push(t) # push it to stack
        else:
            try:
                # getting all useful data
                arg2 = stack.pop()
                oprt = stack.pop()
                arg1 = stack.pop()
                symb = stack.pop()
                # chekc if it is a good end
                if symb != end[t]: return
                # build the current leave of the tree
                tree = BinaryTree(oprt)
                tree.left_node  = arg1
                tree.right_node = arg2
                # push it to the stack
                stack.push(tree)
            except EmptyStackError:
                return
    try:
        output = stack.pop()
        if not stack.is_empty(): return
        return output
    except ValueError:
        return


def parse_tree(expression):
    if any(not(c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|\-|\*|/)').findall(expression)
    print(tokens)
    try:
        value = parse_expression(tokens)
        return value
    except ZeroDivisionError:
        return


parse_tree('{(1 + 20)*(30 - 400)}').print_binary_tree()
#print(parse_tree('{(1 + 20)*(30 - 400)}'))
