class CircularQueue:
    def __init__(self, size=10):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.front = self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def insert(self, item):
        if self.isFull():
            print('Queue is full')

        # for first input
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def delete(self):
        if self.isEmpty():
            print('Queue is empty')
        
        # if we have only one element 
        elif self.front == self.rear:
            removed = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return removed
        
        else:
            removed = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return removed

    def display(self):
        if self.isEmpty():
            print('Queue is empty')
        
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")

        # front = 0, rear=4
        # front=2, rear=0
        else:
            # for i in range(self.front, self.size):
            #     print(self.queue[i], end=" ")
            # for i in range(0, self.rear+1):
            #     print(self.queue[i], end=" ")
            f = self.front
            while f != self.rear:
                print(self.queue[f], end=" ")
                f = (f + 1) % self.size
            print(self.queue[f], end=" ")
        print()

queue = CircularQueue()
for i in range(1, 11):
    queue.insert(i)

queue.display()
print(queue.delete())
queue.display()
queue.insert(11)
queue.display()
print(queue.delete())
queue.display()