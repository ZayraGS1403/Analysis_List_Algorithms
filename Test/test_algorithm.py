import unittest
from List.algorithms import LinkedList, DoublyLinkedList
import random

original_randint = random.randint


class TestList(unittest.TestCase):
    def setUp(self):
        random.randint = lambda a, b: 0
        self.ll = LinkedList()
        self.dll = DoublyLinkedList()

    def tearDown(self):
        random.randint = original_randint

    def test_linked_list_init(self):
        "Verify that LinkedList initializes correctly." ""
        self.assertIsNone(self.ll.head)
        self.assertEqual(self.ll.size, 0)

    def test_linked_list_insert_random(self):
        "Verify that `insert_random` in LinkedList works correctly." ""
        # Insert a value
        self.ll.insert_random(5)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.data, 5)
        self.assertIsNone(self.ll.head.next)

        # Insert another value (fixed position 0)
        self.ll.insert_random(10)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.head.data, 10)  # Debería estar al inicio
        self.assertEqual(self.ll.head.next.data, 5)

        # Insert a third value (fixed position 0)
        self.ll.insert_random(15)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.head.data, 15)  # Debería estar al inicio
        self.assertEqual(self.ll.head.next.data, 10)
        self.assertEqual(self.ll.head.next.next.data, 5)

        # Verify string representation
        self.assertEqual(str(self.ll), "15 -> 10 -> 5")

    def test_linked_list_delete_random(self):
        """Verify that `delete_random` in LinkedList works correctly."""
        # Insert some values first
        self.ll.insert_random(5)  # Posición 0 -> 5
        self.ll.insert_random(10)  # Posición 0 -> 10 -> 5
        self.ll.insert_random(15)  # Posición 0 -> 15 -> 10 -> 5
        self.assertEqual(self.ll.size, 3)

        self.ll.delete_random()
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.head.data, 10)  # Debería quedar 10 -> 5
        self.assertEqual(str(self.ll), "10 -> 5")

        self.ll.delete_random()
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.data, 5)
        self.assertEqual(str(self.ll), "5")

        # delete the last
        self.ll.delete_random()
        self.assertEqual(self.ll.size, 0)
        self.assertIsNone(self.ll.head)

    def test_empty_list_deletion(self):
        """Verify that `delete_random` does not fail on empty lists."""
        self.ll.delete_random()
        self.assertEqual(self.ll.size, 0)
        self.assertIsNone(self.ll.head)

    def test_multiple_insertions_different_positions(self):
        "Verify that `insert_random` works with different positions (using fixed values)."
        random.randint = lambda a, b: a + (b - a) // 2
        self.ll.insert_random(1)  #  (0) -> 1
        self.ll.insert_random(2)  #  (1) -> 2 -> 1
        self.ll.insert_random(3)  #  (1) -> 2 -> 3 -> 1
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(str(self.ll), "2 -> 3 -> 1")
        random.randint = lambda a, b: 0

    # ---Test Doble linked list--------------------------------------------------------------------------------------------------------

    def test_doubly_linked_list_init(self):
        "Verify that `DoublyLinkedList` initializes correctly."
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(self.dll.size, 0)

    def test_doubly_linked_list_insert_random(self):
        "Verify that `insert_random` in `DoublyLinkedList` works correctly."
        # Insert a value
        self.dll.insert_random(5)
        self.assertEqual(self.dll.size, 1)
        self.assertEqual(self.dll.head.data, 5)
        self.assertEqual(self.dll.tail.data, 5)
        self.assertIsNone(self.dll.head.prev)
        self.assertIsNone(self.dll.head.next)

        # Insert another value (posición 0 fija)
        self.dll.insert_random(10)
        self.assertEqual(self.dll.size, 2)
        self.assertEqual(self.dll.head.data, 10)  # Should be at the beginning
        self.assertEqual(self.dll.tail.data, 5)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(self.dll.head.next.data, 5)
        self.assertEqual(self.dll.head.next.prev.data, 10)
        self.assertIsNone(self.dll.tail.next)

        # Insert a third value (posición 0 fija)
        self.dll.insert_random(15)
        self.assertEqual(self.dll.size, 3)
        self.assertEqual(self.dll.head.data, 15)  # Should be at the beginning
        self.assertEqual(self.dll.tail.data, 5)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(self.dll.head.next.data, 10)
        self.assertEqual(self.dll.head.next.next.data, 5)
        self.assertEqual(self.dll.head.next.next.prev.data, 10)
        self.assertIsNone(self.dll.tail.next)

        self.assertEqual(str(self.dll), "15 -> 10 -> 5")

    def test_doubly_linked_list_delete_random(self):
        "Verify that `delete_random` in `DoublyLinkedList` works correctly."
        # Insert some values first
        self.dll.insert_random(5)  # Posición 0 -> 5
        self.dll.insert_random(10)  # Posición 0 -> 10 -> 5
        self.dll.insert_random(15)  # Posición 0 -> 15 -> 10 -> 5
        self.assertEqual(self.dll.size, 3)

        self.dll.delete_random()
        self.assertEqual(self.dll.size, 2)
        self.assertEqual(self.dll.head.data, 10)  # Should be 10 -> 5
        self.assertEqual(self.dll.tail.data, 5)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(self.dll.head.next.data, 5)
        self.assertEqual(self.dll.head.next.prev.data, 10)
        self.assertIsNone(self.dll.tail.next)
        self.assertEqual(str(self.dll), "10 -> 5")

        self.dll.delete_random()
        self.assertEqual(self.dll.size, 1)
        self.assertEqual(self.dll.head.data, 5)
        self.assertEqual(self.dll.tail.data, 5)
        self.assertIsNone(self.dll.head.prev)
        self.assertIsNone(self.dll.head.next)
        self.assertEqual(str(self.dll), "5")

        # Delete the last
        self.dll.delete_random()
        self.assertEqual(self.dll.size, 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_empty_list_deletion_doble_linkend_list(self):
        "Verify that `delete_random` does not fail on empty lists."
        self.dll.delete_random()
        self.assertEqual(self.dll.size, 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_multiple_insertions_different_positions_doble_linkend_list(self):
        "Verify that `insert_random` works with different positions (using fixed values)."
        random.randint = lambda a, b: a + (b - a) // 2
        self.dll.insert_random(1)  #  (0) -> 1
        self.dll.insert_random(2)  #  (1) -> 2 -> 1
        self.dll.insert_random(3)  #  (1) -> 2 -> 3 -> 1
        self.assertEqual(self.dll.size, 3)
        self.assertEqual(
            str(self.dll), "2 -> 3 -> 1"
        )  # Expected order with middle position
        random.randint = lambda a, b: 0


if __name__ == "__main__":
    unittest.main()
