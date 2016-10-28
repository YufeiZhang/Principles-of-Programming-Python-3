# LL = ExtendedLinkedList([3,2,4,1,2,4,1,3]); LL.remove_duplicates(); LL.print()

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            print(current_node.value)
            node = current_node
            while node.next_node:
                print('next ->',node.next_node.value)
                if node.next_node.value == current_node.value:
                    node.next_node = node.next_node.next_node
                else:
                    node = node.next_node
                print('----------------')
            current_node = current_node.next_node
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
