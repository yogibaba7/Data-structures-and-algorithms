""" Implementation of Doubly linked list  """

class Node:

    def __init__(self,item = None,prev=None,next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:

    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n = Node(data,self.start)
        if self.start is not None:
            n.next = self.start
        self.start = n

    def insert_at_last(self,data):
        n = Node(data)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next

            n.prev = temp
            temp.next = n

    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp = self.start
            while temp!=None:
                if temp.item==data:
                    return temp
                temp = temp.next
           
    def insert_after(self,gnode,data):
        if gnode is not None:
            n = Node(data,gnode,gnode.next)

            if gnode.next is not None:
                gnode.next.prev=n
            gnode.next=n
        else:
            return 'node does not exits'
    
    def delete_first(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start = None
        else:
            self.start.next.prev = None
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next!=None:
                temp = temp.next
            temp.next.prev = None
            temp.next = None
    
    def delete_selected(self,gnode):
        if gnode is not None:
            if gnode.prev==None and gnode.next==None:
                self.start = None
            elif gnode.prev==None and gnode.next!=None:
                gnode.next.prev = None
                self.start = gnode.next
            
            elif gnode.prev!=None and gnode.next==None:
                gnode.prev.next =None
                gnode.prev = None
            else:
                gnode.prev.next = gnode.next
                gnode.next.prev = gnode.prev
    def __iter__(self):
        return DLLIterator(self.start)

    def print_all(self):
        temp = self.start
        while temp!=None:
            print(temp.item,end=" ")
            temp = temp.next

class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
                
        


  

dll = DLL()

# dll.insert_at_start(3)
# dll.insert_at_start(4)
dll.insert_at_last(5)
dll.insert_at_last(6)
dll.insert_at_last(7)
dll.insert_at_start(4)
dll.insert_after(dll.search(7),8)
# dll.delete_selected(dll.search(8))
dll.insert_at_last(7)
dll.delete_last()

# dll.print_all()

for i in dll:
    print(i,end=' ')

