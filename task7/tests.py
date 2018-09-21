"""Task7."""

import task2
import unittest


class Tests(unittest.TestCase):

    def test_instance(self):
        """Check instance of class Coffee."""
        self.assertIsInstance(task2.Coffee("1", 1, 1, 1, 1), task2.Coffee)
        self.assertNotIsInstance("123", task2.Coffee)

    def test_equals(self):
        """Check equals of class Coffee."""
        self.assertEqual(task2.Coffee("1", 1, 1, 1, 1).sugar_amount, 1)
        self.assertEqual(task2.Coffee("1", 1, 1, 1, 1).water_amount, 1)
        self.assertEqual(task2.Coffee("1", 1, 1, 1, 1).coffee_amount, 1)
        self.assertEqual(len(task2.Coffee("1", 1, 1, 1, 1).items), 1)

    def test_(self):
        """Check parameters of class Coffee."""
        self.assertFalse(task2.Coffee("1", 1, 1, 1, 1)
                         .fill_the_machine(10, -1, 10))
        self.assertTrue(task2.Coffee("1", 1, 1, 1, 1)
                        .fill_the_machine(10, 10, 10))

    def test_none(self):
        # This functions will never returned anything
        self.assertIsNone(task2.Coffee("1", 1, 1, 1, 1).display_items())
        self.assertIsNone(task2.Coffee("1", 1, 1, 1, 1).display_amount())
