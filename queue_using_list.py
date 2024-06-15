""" Implementation of queue using list """

class Queue:

    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list)==0

    def enqueue(self,data):
        self.list.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.list.pop(0)   
        else:
            raise ValueError('No values in queue')

    def get_front(self):
        if not self.is_empty():
            return self.list[0]  
        else:
            raise ValueError('No values in queue')

    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]  
        else:
            raise ValueError('No values in queue')


    def size(self):
        return len(self.list)

q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.enqueue(7)
print(q.is_empty())
print('Front Item: ',q.get_front(), ' Rear Item : ',q.get_rear())

print('Size Of Queue : ',q.size())