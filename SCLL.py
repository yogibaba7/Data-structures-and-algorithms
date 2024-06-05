""" Implementation of singly circular linked list  """


class Node:

    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class SCL:

    def __init__(self,last=None):
        self.last = last
    def is_empty(self):
        return self.last==None

    def insert_at_first(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next =self.last.next
            self.last.next = n
            self.last = n

    def search(self,data):
        if not self.is_empty():

            temp = self.last.next
            while temp!=self.last:
                if temp.item==data:
                    return temp
                temp = temp.next
            if temp.item==data:
                return temp
        
        else:
            return None

    def insert_after(self,gnode,data):
        n = Node(data)
        if self.last==gnode:
            n.next = self.last.next
            gnode.next =  n
            self.last = n
        elif self.last.next == gnode:
            n.next = self.last.next
            gnode.next = n

        else:
            n.next = gnode.next
            gnode.next = n

    def print(self):
        temp = self.last.next
        while temp!=self.last:
            print(temp.item,end=' ')
            temp = temp.next
        print(temp.item)

    def delete_first(self):
        if self.last is not None:
            if self.last == self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next
        else:
            return None

    def delete_last(self):
        if self.last is not None:
            if self.last == self.last.next:
                self.last = None
            else:
                temp = self.last.next
                while temp.next.next!=self.last:
                    temp = temp.next
                temp.next.next = self.last.next
                self.last = temp.next

    def delete_selected(self,gnode):
            if not self.is_empty():
                if self.last.next==self.last:
                    if self.last.item==gnode.item:
                        self.last=None
                else:
                    if self.last.next.item==gnode.item:
                        self.delete_first()
                    else:
                        temp=self.last.next

                        while temp!=self.last:
                            if temp.next==self.last:
                                if self.last.item==gnode.item:
                                    self.delete_last()
                                break
                            if temp.next.item==gnode.item:
                                temp.next=temp.next.next
                                break
                            temp=temp.next
    
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)

class CLLIterator:
    def __init__(self,start):
        self.current=start 
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        
        return data
            


scl = SCL()

scl.insert_at_first(1)
scl.insert_at_first(2)
scl.insert_at_last(3)
scl.insert_at_first(4)
scl.insert_at_last(5)
scl.insert_at_last(6)
scl.insert_after(scl.search(3),4)
scl.delete_first()
scl.delete_last()
# scl.delete_selected(scl.search(3))
# scl.delete_selected(scl.search(4))
# scl.delete_selected(scl.search(5))
# scl.delete_selected(scl.search(2))




scl.print()

for i in scl:
    print(i,end=' ')