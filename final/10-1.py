from general_tree import *

def print_out(tree):
    _print_out(tree, 0)


def _print_out(tree, level):
    print('\t' * level, end = '')
    print(tree.value)
    for subtree in tree.children:
        _print_out(subtree, level + 1)


def count_tabs(d):
    count = 0
    for ch in d:
        if ch == '\t':
            count += 1
    return count


def build_tree(data, lv):
    line = data.pop()
    try:
        value = int(line[lv:])
    except ValueError:
        return

    tree = GeneralTree(value)
    while data:
        next_lv = count_tabs(data[-1])
        if   next_lv > lv + 1:
            return
        elif next_lv == lv + 1:
            tree.children.append(build_tree(data, lv+1))
        else:
            return tree
    return tree

        
def main():
    lines = open('tree.txt').readlines()
    #print(lines)

    data = []
    for i in range(len(lines)):
        line = lines.pop()
        line = line.rstrip() # here we use rstrip() to replace \n, ' ', \t
        #print(list(line))
        if line:
            data.append(line)
    #print(data)
    
    if not data or count_tabs(data[-1]): return

    tree = build_tree(data, 0)
    #print_out(tree)

    if not tree or data: print('tree.txt does not contain the correct tree.')
    else:                print_out(tree)

        


if __name__ == '__main__':
    main()
