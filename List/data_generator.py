import random
from List.algorithms import LinkedList, DoublyLinkedList
import array
from List.constants import MAX_VALUE


def get_random_linked_list(size, limit=MAX_VALUE):
    ll = LinkedList()
    for _ in range(size):
        ll.insert_random(random.randint(0, limit))
    return ll


def get_random_doubly_linked_list(size, limit=MAX_VALUE):
    dll = DoublyLinkedList()
    for _ in range(size):
        dll.insert_random(random.randint(0, limit))
    return dll


def get_random_array(size, limit=MAX_VALUE):
    arr = array.array("i")
    for _ in range(size):
        arr.append(random.randint(0, limit))
    return arr
