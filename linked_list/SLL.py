
# ----------------------------------------

# defining node class
class node:

    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

# defining singly circular list
class SLL:
    
    def __init__(self,start=None):
        self.start = start
    
    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n = node(data,self.start)
        self.start = n
    
    def insert_at_last(self,data):
        n = node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next= n

    def search(self,data):
        if self.start is not None:
            temp = self.start
            while temp!=None:
                if temp.item ==data:
                    return temp
                temp = temp.next
        else:
            return None
        
    def insert_selected(self,gnode,data):
        
            n = node(data)
            if self.start is None:
                return None
            else:
                n.next = gnode.next
                gnode.next = n
    
    def print_all(self):
        if self.is_empty():
            return 'nothing in list'
        else:
            temp = self.start
            while temp!=None:
                print(temp.item,end=' ')
                temp = temp.next
        
    def delete_first(self):
        if self.is_empty():
            return None
        else:
            self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            return None
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next!=None:

                temp = temp.next
            temp.next = None
    
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
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

        
sll = SLL()


sll.insert_at_last(5)
sll.insert_at_last(6)
sll.insert_at_start(3)
sll.insert_at_start(4)
sll.insert_selected(sll.search(3),6)
sll.insert_selected(sll.search(6),7)
sll.delete_first()
# sll.delete_last()
# sll.delete_last()
sll.delete_item(5)
sll.print_all()
print()

for i in sll:
    print(i,end=' ')

            

                

