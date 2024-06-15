""" Implementation of queue using singly linked list """

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class queue:

    def __init__(self,start=None):
        self.start = start
        self.count_item = 0

    def is_empty(self):
        return self.start==None
    
    def enqueue(self,data):
        n = Node(data,self.start)
        self.start = n
        self.count_item += 1

    def dequeue(self):
        if not self.is_empty():
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.count_item -= 1
        else:
            raise ValueError('No values in queue')

    def get_front(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.data
        else:
            raise ValueError('No values in queue')

    def get_rear(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise ValueError('No values in queue')

    def size(self):
        return self.count_item

q = queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.enqueue(7)



print(q.get_front())
print(q.get_rear())
print(q.size())


# --------- Implementation of queue using singly linked list without traversing ------------ 


class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class QueueS:

    def __init__(self,front=None,rear=None):
        self.front = front
        self.rear = rear
        self.item_count = 0

    def Is_empty(self):
        return self.front==None
    
    def enqueue(self,data):
        n = Node(data)
        if self.Is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count += 1

    def dequeue(self):
        if self.Is_empty():
            raise ValueError("No values in queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if self.Is_empty():
            raise ValueError('No values in Queue')
        else:
            return self.front.item
        
    def get_rear(self):
        if self.Is_empty():
            raise ValueError('No values in Queue')
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count

Q = QueueS()
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
Q.enqueue(8)

print("Front item:",Q.get_front(),' Rear item:',Q.get_rear())
print('Queue Size:',Q.size())
print('Deleted item:',Q.get_front(),Q.dequeue(),' Now Size Of Queue : ',Q.size())




        


