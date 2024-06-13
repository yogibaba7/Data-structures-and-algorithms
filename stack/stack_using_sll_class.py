""" Implementation of Stack using SLL class"""
from SLL import *

class Stackk:

    def __init__(self):
        self.mylist = SLL()
        self.count_item = 0

    def is_empty(self):
        return self.mylist.Is_empty()

    def puush(self,data):
        self.mylist.insert_at_start(data)
        self.count_item += 1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.count_item -= 1
        else:
            raise ValueError("NO items in stack")
    
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise ValueError("NO items in stack")

    def size(self):
        return self.count_item

s = Stackk()
# s.puush(2)
# s.puush(3)
# s.puush(4)
# s.pop()
print(s.size())
print(s.peek())
