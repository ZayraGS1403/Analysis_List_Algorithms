import random

# Node for LinkedList
class Node:
    def __init__(self, data):  # O(1)
        self.data = data  # O(1)
        self.next = None  # O(1)

# Node for DoublyLinkedList
class DoublyNode:
    def __init__(self, data):  # O(1)
        self.data = data  # O(1)
        self.next = None  # O(1)
        self.prev = None  # O(1)

# LinkedList Implementation
class LinkedList:
    def __init__(self):  # O(1)
        self.head = None  # O(1)
        self.size = 0  # O(1)

    def insert_random(self, value):  # Average O(n), Worst O(n)
        new_node = Node(value)  # O(1)
        if not self.head:  # O(1)
            self.head = new_node  # O(1)
        else:
            pos = random.randint(0, self.size)  # O(1)
            if pos == 0:  # O(1)
                new_node.next = self.head  # O(1)
                self.head = new_node  # O(1)
            else:
                current = self.head  # O(1)
                for _ in range(pos - 1):  # O(n)
                    current = current.next  # O(1)
                new_node.next = current.next  # O(1)
                current.next = new_node  # O(1)
        self.size += 1  # O(1)

    def delete_random(self):  # Average O(n), Worst O(n)
        if not self.head:  # O(1)
            return  # O(1)
        pos = random.randint(0, self.size - 1)  # O(1)
        if pos == 0:  # O(1)
            self.head = self.head.next  # O(1)
        else:
            current = self.head  # O(1)
            for _ in range(pos - 1):  # O(n)
                current = current.next  # O(1)
            current.next = current.next.next  # O(1)
        self.size -= 1  # O(1)

    def __str__(self):  # O(n)
        current = self.head  # O(1)
        result = []  # O(1)
        while current:  # O(n)
            result.append(str(current.data))  # O(1)
            current = current.next  # O(1)
        return " -> ".join(result)  # O(n)

# DoublyLinkedList Implementation
class DoublyLinkedList:
    def __init__(self):  # O(1)
        self.head = None  # O(1)
        self.tail = None  # O(1)
        self.size = 0  # O(1)

    def insert_random(self, value):  # Average O(n), Worst O(n)
        new_node = DoublyNode(value)  # O(1)
        if not self.head:  # O(1)
            self.head = self.tail = new_node  # O(1)
        else:
            pos = random.randint(0, self.size)  # O(1)
            if pos == 0:  # O(1)
                new_node.next = self.head  # O(1)
                self.head.prev = new_node  # O(1)
                self.head = new_node  # O(1)
            elif pos >= self.size // 2:  # O(1)
                current = self.tail  # O(1)
                for _ in range(self.size - pos):  # O(n)
                    current = current.prev  # O(1)
            else:
                current = self.head  # O(1)
                for _ in range(pos - 1):  # O(n)
                    current = current.next  # O(1)
            new_node.next = current.next  # O(1)
            new_node.prev = current  # O(1)
            if current.next:
                current.next.prev = new_node  # O(1)
            else:
                self.tail = new_node  # O(1)
            current.next = new_node  # O(1)
        self.size += 1  # O(1)

    def delete_random(self):  # Average O(n), Worst O(n)
        if not self.head:  # O(1)
            return  # O(1)
        pos = random.randint(0, self.size - 1)  # O(1)
        if pos == 0:  # O(1)
            self.head = self.head.next  # O(1)
            if self.head:
                self.head.prev = None  # O(1)
            else:
                self.tail = None  # O(1)
        elif pos >= self.size // 2:  # O(1)
            current = self.tail  # O(1)
            for _ in range(self.size - pos - 1):  # O(n)
                current = current.prev  # O(1)
        else:
            current = self.head  # O(1)
            for _ in range(pos):  # O(n)
                current = current.next  # O(1)
        if current.prev:
            current.prev.next = current.next  # O(1)
        if current.next:
            current.next.prev = current.prev  # O(1)
        else:
            self.tail = current.prev  # O(1)
        self.size -= 1  # O(1)

    def __str__(self):  # O(n)
        current = self.head  # O(1)
        result = []  # O(1)
        while current:  # O(n)
            result.append(str(current.data))  # O(1)
            current = current.next  # O(1)
        return " -> ".join(result)  # O(n)

# Complexity Summary:
# - LinkedList:
#   - Random Insert: O(n)
#   - Random Delete: O(n)
#
# - DoublyLinkedList:
#   - Random Insert: O(n)
#   - Random Delete: O(n)