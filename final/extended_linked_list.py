from linked_list import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        if not self.head:
            return
        current_node = self.head
        
        while current_node:
            node = current_node
            
            while node.next_node:
                if node.next_node.value == current_node.value:
                    # if it is redundant, then point point next_node to next_node.next_node
                    node.next_node = node.next_node.next_node
                else:
                    node = node.next_node
                    
            current_node = current_node.next_node
                
LL = ExtendedLinkedList([3,2,4,1,2,4,1,3]); LL.remove_duplicates(); LL.print()
