"""  Implementation of  stack inheriting sll linked list class """

from SLL import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.count_item = 0

    def is_empty(self):
        return self.is_empty()

    def push(self,data):
        self.insert_at_start(data)
        self.count_item += 1

    def pop(self):
        if not self.Is_empty():
            self.delete_first()
            self.count_item -= 1
        else:
            raise ValueError('No values In stack')

    def peek(self):
        if not self.Is_empty():
            return self.start.item
        else:
            raise ValueError('No values In stack')
        
    
    def size(self):
        return self.count_item

    def insert_at_last(self,data):
        raise AttributeError('No attribute')

    def insert_selected(self,gnode,data):
        raise AttributeError('No attribute')

    def delete_last(self):
        raise AttributeError('No attribute')

    def delete_item(self,data):
        raise AttributeError('No attribute')

    def print_all(self):
        raise AttributeError('No attribute')

s = Stack()

s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()

print(s.size())
print(s.peek())

# s.delete_last()
# s.delete_item(3)
# s.insert_at_last(5)