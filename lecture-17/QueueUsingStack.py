# insert: O(N)
# removal: O(1)
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def insert(self, item):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(item)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())        

    def remove(self):
        if len(self.stack1) == 0:
            print('Queue is Empty')
            return
        return self.stack1.pop()


# insert: O(1)
# removal: O(N)
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def insert(self, item):
        self.stack1.append(item)

    def remove(self):
        if len(self.stack1) == 0:
            print('Queue is Empty')
            return
        
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        
        removed = self.stack2.pop()
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        return removed