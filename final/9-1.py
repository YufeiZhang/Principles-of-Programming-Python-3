import re
from operator import add, sub, mul, truediv
from array_stack import ArrayStack, EmptyStackError


def calculate(tokens):
    end = {')':'(', ']':'[', '}':'{'}
    operate = {'+': add, '-': sub, '*': mul, '/': truediv}
    stack = ArrayStack()
    #print(stack._data)

    for t in tokens:
        try:
            t = int(t)
        except ValueError:
            pass

        if t not in end:
            stack.push(t)
        else:
            #print(stack._data,'-----')
            try:
                arg2 = stack.pop()
                oprt = stack.pop()
                arg1 = stack.pop()
                symb = stack.pop()
                if symb != end[t]: return
                else:
                    stack.push(operate[oprt](arg1,arg2))
            except EmptyStackError:
                return
    #print(stack._data)
    try:
        num = stack.pop()
        if not stack.is_empty(): return
        return num
    except ValueError:
        return
        
    
def evaluate(expression):
    '''
    evaluate('{1 + [((20*30)-400) / 500]}')
    1.4
    '''
    if any(not(c.isdigit() or c.isspace() or c in'()[]{}+-*/') for c in expression):
        print('Your input is bad.')
        return

    #tokens = re.compile('()').findall(expression)
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|\-|\*|/)').findall(expression)
    #print(tokens)

    try:
        value = calculate(tokens)
        return value
    except ZeroDivisionError:
        print('Divisior cannot be zero.')
        return


print(evaluate('{1 + [((20*30)-400) / 500]}'))
