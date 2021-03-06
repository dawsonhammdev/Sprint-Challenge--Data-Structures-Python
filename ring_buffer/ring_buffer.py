class RingBuffer:
        def __init__(self, capacity):
                self.data = []
                self.capacity = capacity
                self.cur=0

        def append(self, item):
                ## append an element overwriting the oldest one
                if len(self.data) == self.capacity:
                        self.cur = 0
                        self.data[self.cur]=item
                        self.cur=(self.cur+1)%self.capacity
                        self.__class__=bufferfull
                else:
                        self.data.append(item)

        def get(self):
                return self.data

class bufferfull:

        def append(self,item):
                if len(self.data) < self.capacity:
                        self.data.insert(self.cur, item)
                else:
                        self.data[self.cur]=item
                        self.cur=(self.cur+1)%self.capacity

        def remove(self,item):
                if self.data:
                        if self.capacity > len(self.data):
                                self.cur=0
                        self.data.pop(self.cur)

        def get(self):
                return self.data[:self.cur]+self.data[self.cur:]

