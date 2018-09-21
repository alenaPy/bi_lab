"""Tests for py_tasks."""
from unittest import TestCase

import pytask


class TestPytask(TestCase):

    def setUp(self):
        """Init."""

    def test_generate_numbers(self):
        """Test for function generate_numbers."""
        true_dict1 = {1: 1, 2: 4}
        true_dict2 = {1: 1, 2: 4, 3: 9, 4: 16}
        self.assertEqual(pytask.generate_numbers(2), true_dict1)
        self.assertEqual(pytask.generate_numbers(4), true_dict2)

    def test_count_characters(self):
        """Test for function count_characters."""
        true_dict1 = {'a': 1, ' ': 5}
        true_dict2 = {'a': 3, 'b': 3, 'c': 2, '_': 2}
        self.assertEqual(
            pytask.count_characters('a     '), true_dict1)
        self.assertEqual(
            pytask.count_characters('abc_cbb_aa'), true_dict2)

    def test_is_palindrome(self):
        """Test for function is_palindrome."""
        self.assertTrue(pytask.is_palindrome('aaaa   b   aaaa'))
        self.assertFalse(pytask.is_palindrome('awkqwekwk wadkadk dkdkfeepqqw'))

    def test_fizzbuzz(self):
        """Test for function fizzbuzz."""
        self.assertEqual(pytask.fizzbuzz(7), 7)
        self.assertEqual(pytask.fizzbuzz(99), 'Fizz')

    def tearDown(self):
        """Finish"""
