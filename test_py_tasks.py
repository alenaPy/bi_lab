"""Tests."""
import py_tasks

from unittest import TestCase


class TestPyTasks(TestCase):

    def test_is_palindrome(self):
        """Test for is_palindrome."""
        self.assertFalse(py_tasks.is_palindrome('Python :)'))
        self.assertTrue(py_tasks.is_palindrome('123aa321'))

    def test_fizzbuzz(self):
        """Test for fizzbuzz."""
        self.assertEqual(py_tasks.fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(py_tasks.fizzbuzz(2), 2)

    def test_count_characters(self):
        """Test for count_characters."""
        self.assertEqual(
            py_tasks.count_characters('dheeerrraannnaannaannaa', 'a'), 8)
        self.assertEqual(
            py_tasks.count_characters('qwerty33', '3'), 2)

    def test_number_square(self):
        """Test for number_square."""
        self.assertEqual(py_tasks.number_square(5), 25)
        self.assertEqual(py_tasks.number_square(12), 144)

    def tearDown(self):
        """Finish"""
