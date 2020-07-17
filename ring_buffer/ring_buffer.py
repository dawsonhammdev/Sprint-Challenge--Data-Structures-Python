class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

# we would start like this: [None None None None]

    def append(self, item):
        # set item to equal the current in storage
        self.storage[self.current] = item
        # append 1 on to current
        self.current += 1
        # if current is equal to capacity then current is zero
        if self.current == self.capacity:
            self.current = 0
    def get(self):
        # return a for loop for all the items in storage that have a value
        return [x for x in self.storage if x is not None]
