""" Implementation of queue using sll class """

from SLL import *

class Queue:

    def __init__(self):
        self.list = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.list.is_empty()

    def enqueue(self,data):
        self.list.insert_at_start(data)
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            self.list.delete_last()
            self.item_count -= 1
        else:
            raise ValueError('No values in queue')

    def get_front(self):
        if not self.is_empty():
            temp = self.list.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise ValueError('No values in queue')

    def get_rear(self):
        if not self.is_empty():
            return self.list.start.item
        else:
            raise ValueError('No values in queue')

    def size(self):
        return self.item_count

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.enqueue(8)
q.dequeue()

print(q.is_empty())
print('Front Item: ',q.get_front(), ' Rear Item : ',q.get_rear())

print('Size Of Queue : ',q.size())



    
