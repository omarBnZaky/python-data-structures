class Stack:
    def __init__(self):
        self.items = []
        self.top = 0
        #top is about the length not the index
    
    def push(self,item):
        self.items.append(item)
        self.top = self.top +1
    
    def pop(self):
        deleted = self.items[self.top - 1]
        del self.items[self.top - 1]
        self.top = self.top - 1
        return deleted

    def stack_top_element(self):
        if not self.top == 0 :
            return self.items[self.top-1]
        else:
            return 0

    def is_empty(self):
        return self.top == 0

    def get_stack(self):
        return self.items

"""
s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("c")
s.push("d")
print(s.get_stack())
print(s.pop())
print(s.get_stack())
print(s.stack_top_element())
print(s.is_empty())
s.pop()
s.pop()
s.pop()
print(s.is_empty())
print(s.stack_top_element())
"""