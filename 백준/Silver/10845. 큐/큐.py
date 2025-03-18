class Queue:
    def __init__(self):
        self.container = list()
        self.result = list()
        self.size = 0
    def push(self, x):
        (self.container).append(x)
        self.size += 1
    def pop(self):
        if self.size == 0: (self.result).append(-1)
        else:
            (self.result).append(self.container[0])
            del self.container[0]
            self.size -= 1
    def front(self):
        if self.size == 0: (self.result).append(-1)
        else: (self.result).append(self.container[0])
    def back(self):
        if self.size == 0: (self.result).append(-1)
        else: (self.result).append(self.container[self.size-1])
    def empty(self):
        if self.size == 0:
            (self.result).append(1)
        else: (self.result).append(0)
    def size_(self):
        (self.result).append(self.size)

if __name__ == '__main__':
    queue = Queue()
    num = int(input())
    for _ in range(num):
        I = (input()).split()
        if len(I)==2: I[1]=int(I[1])
        if I[0] == 'push':
            queue.push(I[1])
        elif I[0] == 'front':
            queue.front()
        elif I[0] == 'back':
            queue.back()
        elif I[0] == 'size':
            queue.size_()
        elif I[0] == 'pop':
            queue.pop()
        elif I[0] == 'empty':
            queue.empty()
    for elem in queue.result:
        print(elem)