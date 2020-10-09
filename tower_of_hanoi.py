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
    source_rod = Stack()
    auxiliary_rod = Stack()
    destination_rod = Stack()

    def tower_of_hanoi(disks, source, destination, auxiliary):
        if disks == 1:
            source.pop()
            destination.push('disk 1')
            print(destination)
        elif disks > 1:
            tower_of_hanoi(disks - 1, source=source, destination=auxiliary, auxiliary=destination)
            source.pop()
            destination.push(f'disk {disks}')
            print(destination)
            tower_of_hanoi(disks - 1, source=auxiliary, destination=destination, auxiliary=source)


    no_of_disks = int(input('Enter the number of the disks : '))
    assert no_of_disks > 0, 'Number of disks cannot be less than 1'
    for i in reversed(range(1, no_of_disks+1)):
        source_rod.push(f'disk {i}')

    print('Before: ', end='')
    print(source_rod, end=' - ')
    print(auxiliary_rod, end=' - ')
    print(destination_rod)
    tower_of_hanoi(no_of_disks, source_rod, destination_rod, auxiliary_rod)
    print('After: ', end='')
    print(source_rod, end=' - ')
    print(auxiliary_rod, end=' - ')
    print(destination_rod)
