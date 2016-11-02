from general_tree import *

def count_tabs(d):
    count = 0
    for ch in d:
        if ch == '\t':
            count += 1
    return count


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
    print(data)
    
    if not data or count_tabs(data[-1]): return

    tree = build_tree(data, 0)

    if not tree or data: return
    else:                return tree

        


if __name__ == '__main__':
    main()
