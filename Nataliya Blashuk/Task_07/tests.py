"""Unittests for functions from pytasks.py."""

import pytasks_t

from unittest import TestCase


class PytasksUnittest(TestCase):
    """Class definition."""

    def set_up(self):
        """Init class."""

    def count_characters_test(self):
        """Unittest for count_characters."""
        self.assertEqual(pytasks_t.count_characters(
            "abcdefgabc", "a"), 2)
        self.assertEqual(pytasks_t.count_characters(
            "ftyr567sss", "s"), 3)

    def fizz_buzz_test(self):
        """Unittest for fizz_buzz."""
        self.assertEqual(pytasks_t.fizz_buzz(45), "FizzBuzz")
        self.assertEqual(pytasks_t.fizz_buzz(3), "Fizz")
        self.assertEqual(pytasks_t.fizz_buzz(5), "Buzz")
        self.assertEqual(pytasks_t.fizz_buzz(7), 7)

    def is_palindrome_test(self):
        """Unittest for is_palindrome."""
        self.assertEqual(pytasks_t.is_palindrome("Red rum, sir, is murder"))
        self.assertEqual(pytasks_t.is_palindrome("Kiol, kdx"))

    def square_number_test(self):
        """Unittest for square_number."""
        self.assertEqual(pytasks_t.square_number(4), 16)
        self.assertEqual(pytasks_t.square_number(3), 10)

    def tearDown(self):
        """Finish class."""
