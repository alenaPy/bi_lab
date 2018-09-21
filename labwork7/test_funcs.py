from unittest import TestCase

import functions


class TestPyTasks(TestCase):

    def setUp(self):
        """Init."""

    def test_is_palindrome(self):
        """Test for is_palindrome."""
        self.assertFalse(functions.isPalindrome('An apple a day keeps the '
                                                'doctor away'))
        self.assertTrue(functions.isPalindrome('QwErTytrewq'))

    def test_fizzbuzz(self):
        """Test for fizzbuzz."""
        self.assertEqual(functions.fizz_buzz(25), 'Buzz')
        self.assertEqual(functions.fizz_buzz(1), 1)

    def test_count_characters(self):
        """Test for count_characters."""
        self.assertEqual(
            functions.count_characters('sbdvbadlfbvdhfs', 's'), 2)
        self.assertEqual(
            functions.count_characters('dfjkvndfjvnfvnfj', 'j'), 3)

    def test_generate_numbers(self):
        """Test for number_square."""
        self.assertEqual(functions.generate_numbers(5), 25)
        self.assertEqual(functions.generate_numbers(7), 49)

    def tearDown(self):
        """Finish"""
