class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    """ insertion methods"""
    def prepend(self,data):
        #add the node to the start of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        #add the node to the end of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self,prev_node,data):
        if not prev_node:
            raise ("Previous Node not in the list")
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    """Deletion Methods """
    def delete_node(self,key):
        cur_node = self.head
        if cur_node and  cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = prev.next

        if cur_node is not None:
            prev.next = cur_node.next
        
    def delete_node_at_postion(self,pos):
        cur_node = self.head
        if pos == 0:
            cur_node = cur_node.next
            return
        prev = None
        count = 1
        while cur_node and count !=pos:
            prev = cur_node
            cur_node = prev.next
            count+=1
        
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    """ Length Methods"""
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count+=1
            cur_node = cur_node.next
        return count

    def len_recursive(self,node):
        if node is None:
            return 0 
        return 1 + self.len_recursive(node.next)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("D")
llist.append("C")
llist.prepend("J")
llist.insert_after_node(llist.head.next,"R")
llist.delete_node("A")
llist.delete_node_at_postion(0)
llist.print_list()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))