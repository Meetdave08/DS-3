# 3031varun
class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def len(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]

    def dequeue(self):

        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


class DEQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
        self._back = 0

    def last(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._back]

    def enqueue_front(self, e):
        self.enqueue(e)
        self._back = (self._front + self._size - 1) % len(self._data)

    def enqueue_back(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def dequeue_front(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def dequeue_back(self):
        answer = self.dequeue()
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def _resize(self, cap):
        ArrayQueue._resize(self, cap)
        self._back = (self._front + self._size - 1) % len(self._data)

    def show_all(self):
        print(f"Size: {self._size}", end=', ')
        print(f"Front: {self._front}", end=', ')
        print(f"Back: {self._back}", end=', ')
        try:
            print("First: ", self.first(), end=', ')
            print("Last: ", self.last(), end=',\n')
        except:
            print("Queue is empty")
        print(f"Queue: {self._data}")


if __name__ == "__main__":
    deq = DEQueue()
    for i in range(1, 4):
        deq.enqueue_front("f_" + str(i))
        deq.show_all()
    for i in range(1, 4):
        deq.dequeue_front()
        deq.show_all()
    for i in range(1, 4):
        deq.enqueue_back("b_" + str(i))
        deq.show_all()
    for i in range(1, 4):
        deq.dequeue_back()
        deq.show_all()
    for i in range(1, 13):
        deq.enqueue_front("f_" + str(i))
        deq.show_all()
    for i in range(1, 11):
        deq.enqueue_back("b_" + str(i))
        deq.show_all()
    for i in range(1, 13):
        deq.dequeue_front()
        deq.show_all()
    for i in range(1, 11):
        deq.dequeue_back()
        deq.show_all()
