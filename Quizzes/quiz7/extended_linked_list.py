# Written by *** for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
    	node = self.head
    	#print(node.value)
    	body = [node.value]
    	for i in range(1, len(self)):
    		node = node.next_node
    		#print(node.value)
    		body.append(node.value)
    	print(body)




    	pass

    
    
