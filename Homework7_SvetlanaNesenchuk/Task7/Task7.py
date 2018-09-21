"""Tests fot the functions."""


from unittest import TestCase

import pytasks


class Tests(TestCase):
    """Tests for pytasks functions."""

    def setUp(self):
        """Init."""

    def test_is_palindrome(self):
        """Test for function is_palindrome."""
        self.assertTrue(pytasks.is_palindrome('aaabbbaaa'))
        self.assertFalse(pytasks.is_palindrome('gdy sfdgys ey eyf'))

    def test_count_characters(self):
        """Test for count_characters."""
        """Test for function count_characters."""
        dict1 = {'c': 3, 'a': 2}
        dict2 = {'c': 3, 'b': 1, 'w': 2, 't': 2}
        self.assertEqual(
            pytasks.count_character('cccaa'), dict1)
        self.assertEqual(
            pytasks.count_character('cccbttww'), dict2)

    def test_fizz_buzz(self):
        """Test for fizz buzz."""
        self.assertEqual(pytasks.fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(pytasks.fizzbuzz(5), 'Buzz')

    def test_generate_numbers(self):
        """Test for function generate_numbers."""
        true_dict1 = {1: 1, 2: 4, 3: 9}
        true_dict2 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
        self.assertEqual(pytasks.generate_numbers(3), true_dict1)
        self.assertEqual(pytasks.generate_numbers(6), true_dict2)

    def tearDown(self):
        """Finish."""
