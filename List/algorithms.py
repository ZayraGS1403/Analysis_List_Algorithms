import random


# Nodo para LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Nodo para DoublyLinkedList
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_random(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            pos = random.randint(0, self.size)
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for _ in range(pos - 1):
                    current = current.next
                new_node.next = current.next
                current.next = new_node
        self.size += 1

    def delete_random(self):
        if not self.head:
            return
        pos = random.randint(0, self.size - 1)
        if pos == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


# DoublyLinkedList
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_random(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            pos = random.randint(0, self.size)
            if pos == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif pos >= self.size // 2:  # Si la posición está más allá de la mitad
                current = self.tail
                for _ in range(self.size - pos):
                    current = current.prev
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
            else:  # Si la posición está en la primera mitad
                current = self.head
                for _ in range(pos - 1):
                    current = current.next
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
        self.size += 1

    def delete_random(self):
        if not self.head:
            return
        pos = random.randint(0, self.size - 1)

        if pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif pos >= self.size // 2:
            current = self.tail
            for _ in range(self.size - pos - 1):
                current = current.prev
        else:
            current = self.head
            for _ in range(pos):
                current = current.next

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        self.size -= 1

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
