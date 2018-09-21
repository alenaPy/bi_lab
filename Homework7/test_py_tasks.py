"""Tests for py_tasks."""
from unittest import TestCase

import py_tasks


class TestPyTasks(TestCase):

    def setUp(self):
        """Init."""

    def test_is_palindrome(self):
        """Test for is_palindrome."""
        self.assertFalse(py_tasks.is_palindrome('sdsdqqdwdsfx'))
        self.assertTrue(py_tasks.is_palindrome('Never odd or even'))

    def test_fizzbuzz(self):
        """Test for fizzbuzz."""
        self.assertEqual(py_tasks.fizzbuzz(100), 'Buzz')
        self.assertEqual(py_tasks.fizzbuzz(1), 1)

    def test_count_characters(self):
        """Test for count_characters."""
        self.assertEqual(
            py_tasks.count_characters('aaaaaaasfdffdfeo;om  mol;95343  '
                                      'grfhfgfea', 'a'), 8)
        self.assertEqual(
            py_tasks.count_characters('hjtyjyjk2312q4  fh6..,,m,bnvaxxw'
                                      'qdwf', '2'), 2)

    def test_number_square(self):
        """Test for number_square."""
        self.assertEqual(py_tasks.number_square(4), 16)
        self.assertEqual(py_tasks.number_square(9), 81)

    def tearDown(self):
        """Finish"""
