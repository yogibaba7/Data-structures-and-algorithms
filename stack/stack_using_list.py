"""implementation of stack"""


class Stack:

    def __init__(self):
        self.liste = []

    def push(self,item):
        self.liste.append(item) 
    
    def pop(self):
        if not len(self.liste)==0:
            self.liste.pop()
        else:
            raise ValueError('No values in stack')
    def is_empty(self):
        if len(self.liste)==0:
            return True
        else:
            return False
    
    def peek(self):
        if not self.is_empty():
            return self.liste[-1]
        else:
            raise ValueError('No values in stack')
    
    def size(self):

        count = 0
        for i in self.liste:
            count += 1
        return count

stack = Stack()

# stack.push(1)
# stack.push(3)
# stack.push(2)
# stack.pop()

print(stack.size())


print(stack.is_empty())
print(stack.peek())


