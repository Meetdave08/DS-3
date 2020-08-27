# 3031varun
class DoublyNode:
    def __init__(self, element, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev

    def display(self):
        print(self.element)


class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0
    
    def get_size(self) -> int:
        return self.__size

    def display(self):
        if self.__size == 0:
            print("Doubly Linked List is empty")
            return
        first = self.__head
        print("The List: ", end='')
        print("["+first.element, end='')
        first = first.next
        while first:
            print(", "+first.element, end='')
            first = first.next
        print("]")

    def add_head(self, e):
        old_head = self.__head
        self.__head = DoublyNode(e)
        self.__head.next = old_head
        if old_head is not None:
            old_head.prev = self.__head
        if self.__tail is None:
            self.__tail = self.__head
        self.__size += 1

    def get_head(self) -> DoublyNode:
        return self.__head

    def remove_head(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
        self.__size -= 1

    def add_tail(self, e):
        new_value = DoublyNode(e)
        if self.get_tail() is not None:
            old_tail = self.__tail
            self.__tail = new_value
            self.__tail.prev = old_tail
            old_tail.next = self.__tail
            self.__size += 1
        else:
            self.add_head(e)

    def get_tail(self) -> DoublyNode:
        return self.__tail

    def remove_tail(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
        self.__size -= 1

    def add_between_list(self, position, element):
        if position > self.__size or position < 0:
            print("Index out of bounds")
        elif position == self.__size:
            self.add_tail(element)
        elif position == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position - 1)
            current_node = self.get_node_at(position)
            new_value = DoublyNode(element)
            prev_node.next = new_value
            new_value.next = current_node
            new_value.prev = prev_node
            current_node.prev = new_value
            self.__size += 1

    def get_node_at(self, index) -> DoublyNode:
        element_node = self.__head
        counter = 0
        if index < 0 or index >= self.__size:
            print("Index out of bounds")
            return None
        while counter < index:
            element_node = element_node.next
            counter += 1
        return element_node

    def remove_between_list(self, position):
        if position < 0 or position >= self.__size:
            print("Index out of bounds")
        elif position == self.__size - 1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position - 1)
            next_node = self.get_node_at(position + 1)
            prev_node.next = next_node
            next_node.prev = prev_node
            self.__size -= 1

    def search(self, search_value) -> bool:
        index = 0
        while index < self.__size:
            value = self.get_node_at(index)
            if value.element == search_value:
                print("Found value '" + str(search_value) + "' at location: " + str(index))
                return True
            index += 1
        print("Couldn't find value '" + str(search_value) + "'")
        return False

    def merge(self, linked_list_value):
        if not self.is_empty():
            last_node = self.get_tail()
            last_node.next = linked_list_value.__head
            if not linked_list_value.is_empty():
                linked_list_value.__head.prev = last_node
                self.__tail = linked_list_value.__tail
            self.__size = self.__size + linked_list_value.__size
        else:
            self.__head = linked_list_value.__head
            self.__tail = linked_list_value.__tail
            self.__size = linked_list_value.__size


if __name__ == "__main__":

    dll = DoublyLinkedList()
    print(dll.is_empty())
    dll.add_between_list(0, "zero")
    dll.add_between_list(1, "one")
    dll.add_between_list(2, "two")
    dll.display()
    print(dll.is_empty())
    print("After removing")
    dll.remove_between_list(1)
    dll.display()

    dll2 = DoublyLinkedList()
    dll2.add_head("first_name")
    dll2.add_tail("last_name")
    print("Head: ", end='')
    dll2.get_head().display()
    print("Tail: ", end='')
    dll2.get_tail().display()
    dll2.remove_tail()
    dll2.get_tail().display()
    dll2.remove_head()
    try:
        dll2.get_head().display()
    except AttributeError as e:
        print(e, "\nNo head found")
    dll2.display()

    dll3 = DoublyLinkedList()
    dll3.add_between_list(0, "zero")
    dll3.add_between_list(1, "one")
    dll3.add_between_list(2, "two")
    dll3.add_between_list(3, "three")
    dll3.display()
    dll3.search("two")
    dll3.search("four")
    dll3.get_node_at(3).display()

    dll4 = DoublyLinkedList()
    dll4.add_between_list(0, "0")
    dll4.add_between_list(1, "1")
    dll4.add_between_list(2, "2")
    dll4.add_between_list(3, "4")
    print("The Two Lists: ")
    dll3.display()
    print("Head: ", end='')
    dll3.get_head().display()
    print("Tail: ", end='')
    dll3.get_tail().display()
    dll4.display()
    print("Head: ", end='')
    dll4.get_head().display()
    print("Tail: ", end='')
    dll4.get_tail().display()
    dll3.merge(dll4)
    print("After Merging")
    dll3.display()
    print("Head: ", end='')
    dll3.get_head().display()
    print("Tail: ", end='')
    dll3.get_tail().display()
    print(f"Size: {dll3.get_size()}", end='')
