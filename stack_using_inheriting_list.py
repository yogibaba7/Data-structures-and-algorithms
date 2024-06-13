"""   Implementation of stack using inheriting list   """

class Stack(list):
    
    def Is_empty(self):
        return len(self)==0

    def Push(self,data):
        self.append(data)

    def poop(self):
        if not self.Is_empty():
            super.pop()
        else:
            raise ValueError("Empty Stack")

    def peek(self):
        if not self.Is_empty():
            return self[-1]
        else:
            raise ValueError('Empty Stack')

    def size(self):
        return len(self)

    def insert(self,index,data):
        raise AttributeError('NO Insert Function For Stack')

stack = Stack()
stack.Push(4)
stack.Push(2)
stack.Push(3)
stack.Push(5)
stack.Push(6)
stack.Push(7)
stack.pop()
stack.pop()



print(stack.peek())
print(stack.size())