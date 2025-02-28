import unittest
from List.data_generator import (
    get_random_linked_list,
    get_random_doubly_linked_list,
    get_random_array,
)
from List.algorithms import LinkedList, DoublyLinkedList
import array
import random

original_randint = random.randint


class TestDataGenerator(unittest.TestCase):
    def setUp(self):
        random.randint = lambda a, b: 42
        self.limit = 100

    def tearDown(self):
        random.randint = original_randint

    def test_get_random_linked_list_empty(self):
        ll = get_random_linked_list(0, limit=self.limit)
        self.assertIsInstance(ll, LinkedList)
        self.assertEqual(ll.size, 0)
        self.assertIsNone(ll.head)
        self.assertEqual(str(ll), "")

    ##-------------------
    def test_get_random_doubly_linked_list_empty(self):
        dll = get_random_doubly_linked_list(0, limit=self.limit)
        self.assertIsInstance(dll, DoublyLinkedList)
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(str(dll), "")

    ##-------------------
    def test_get_random_array(self):
        size = 3
        arr = get_random_array(size, limit=self.limit)

        self.assertIsInstance(arr, array.array)
        self.assertEqual(arr.typecode, "i")
        self.assertEqual(len(arr), size)
        for value in arr:
            self.assertEqual(value, 42)

    def test_get_random_array_empty(self):
        arr = get_random_array(0, limit=self.limit)
        self.assertIsInstance(arr, array.array)
        self.assertEqual(arr.typecode, "i")
        self.assertEqual(len(arr), 0)
        self.assertEqual(list(arr), [])

    def test_get_random_array_different_limit(self):
        size = 2
        custom_limit = 50
        random.randint = lambda a, b: 42
        arr = get_random_array(size, limit=custom_limit)

        self.assertIsInstance(arr, array.array)
        self.assertEqual(arr.typecode, "i")
        self.assertEqual(len(arr), size)
        for value in arr:
            self.assertEqual(value, 42)
            self.assertLessEqual(value, custom_limit)


if __name__ == "__main__":
    unittest.main()
