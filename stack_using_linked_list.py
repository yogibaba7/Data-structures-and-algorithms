""" Implementation using Singly Linked list """

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self,top=None):
        self.top = top
        self.Count = 0

    def Is_empty(self):
        return self.top==None
    
    def Push(self,data):
        n = Node(data,self.top)
        if self.top==None:
            self.top=n
            self.Count += 1
        else:
            
            self.top  = n
            self.Count += 1
    
    def Pop(self):
        if not self.Is_empty():
            self.top = self.top.next
            self.Count -= 1
        else:
            raise ValueError("Stack Is Empty")

    def Peek(self):
        if not self.Is_empty():
            return self.top.data
        else:
            raise ValueError("Stack is Empty")

    def size(self):
        return self.Count

stack = Stack()
stack.Push(5)
stack.Push(6)
stack.Pop()
stack.Push(7)
stack.Push(8)

stack.Pop()
print(stack.size())


print(stack.Peek())





    
