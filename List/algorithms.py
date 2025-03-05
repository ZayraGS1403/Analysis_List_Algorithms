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

    def insert_random(self, value): # O(n)
        new_node = Node(value) # O(1)
        if not self.head:
            self.head = new_node # O(1)
        else:
            pos = random.randint(0, self.size) # O(1)
            if pos == 0:
                new_node.next = self.head   # O(1)
                self.head = new_node       # O(1)
            else:
                current = self.head # O(1)
                for _ in range(pos - 1): # O(n)
                    current = current.next # O(1)
                new_node.next = current.next # O(1)
                current.next = new_node # O(1)
        self.size += 1

    def delete_random(self): # O(n)
        if not self.head: # O(1)
            return # O(1)
        pos = random.randint(0, self.size - 1) # O(1)
        if pos == 0: # O(1)
            self.head = self.head.next # O(1)
        else:
            current = self.head # O(1)
            for _ in range(pos - 1): # O(n)
                current = current.next # O(1)
            current.next = current.next.next # O(1)
        self.size -= 1

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


# DoublyLinkedList
class DoublyLinkedList: # O(n)
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_random(self, value): # O(n)
        new_node = DoublyNode(value) # O(1)
        if not self.head: # O(1)
            self.head = self.tail = new_node # O(1)
        else:
            pos = random.randint(0, self.size) # O(1)
            if pos == 0: # O(1)
                new_node.next = self.head # O(1)
                self.head.prev = new_node # O(1)
                self.head = new_node # O(1)
            elif pos >= self.size // 2:  # Si la posición está más allá de la mitad
                current = self.tail     # O(1)
                for _ in range(self.size - pos): # O(n)
                    current = current.prev # O(1)
                new_node.next = current.next # O(1)
                new_node.prev = current # O(1)
                if current.next: # O(1)
                    current.next.prev = new_node # O(1)
                else:
                    self.tail = new_node # O(1)
                current.next = new_node # O(1)
            else:  # Si la posición está en la primera mitad
                current = self.head
                for _ in range(pos - 1): # O(n)
                    current = current.next # O(1)
                new_node.next = current.next # O(1)
                new_node.prev = current # O(1)
                if current.next: # O(1)
                    current.next.prev = new_node # O(1)
                else:
                    self.tail = new_node # O(1)
                current.next = new_node
        self.size += 1

    def delete_random(self): # O(n)
        if not self.head: # O(1)
            return
        pos = random.randint(0, self.size - 1)  # O(1)

        if pos == 0:
            self.head = self.head.next # O(1)
            if self.head:
                self.head.prev = None # O(1)
            else:
                self.tail = None
        elif pos >= self.size // 2:
            current = self.tail
            for _ in range(self.size - pos - 1): # O(n)
                current = current.prev # O(1)
        else:
            current = self.head # O(1)
            for _ in range(pos): # O(n)
                current = current.next

        if current.prev:
            current.prev.next = current.next # O(1)
        if current.next:
            current.next.prev = current.prev # O(1)
        else:
            self.tail = current.prev # O(1)

        self.size -= 1

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
