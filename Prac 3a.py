# 3031varun
class Stack:
    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]

    def push(self, element):
        self._data.append(element)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self._size -= 1
        return self._data.pop()


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    for i in range(10):
        stack.push(i)
    print(stack.top())
    print(stack)
    print(stack.is_empty())
    for i in range(10):
        print(stack.pop())
    print(stack.is_empty())
