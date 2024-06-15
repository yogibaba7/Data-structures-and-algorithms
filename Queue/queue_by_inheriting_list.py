""" Implementation of queue by inheriting list class """

class Queue(list):

    def is_empty(self):
        return len(self)==0

    def enqueue(self,data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise ValueError('No values in queue')

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise ValueError('No values in queue')

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise ValueError('No values in queue')
    
    def size(self):
        return len(self)

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
print(q.is_empty())
print('Front Item: ',q.get_front(), ' Rear Item : ',q.get_rear())

print('Size Of Queue : ',q.size())


    
