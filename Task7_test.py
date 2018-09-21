"""Task7.test."""


from unittest import TestCase

import Task7


class TestPyTasks(TestCase):
    """TestPyTasks."""

    def setUp(self):
        """SetUp."""
    def test_palindrome(self):
        """Test for is_palindrome."""
        self.assertFalse(Task7.ispalindrome('congratulations'))
        self.assertTrue(Task7.ispalindrome('Dammit I\'m Mad'))

    def test_third_power(self):
        """Test for number_square."""
        self.assertEqual(Task7.third_power(6), 216)
        self.assertNotEqual(Task7.third_power(8), 4096)

    def test_count_characters(self):
        """Test for count_characters."""
        self.assertEqual(
            Task7.character_count('Rock Paper Scissors Lizzard Spok', 'o'), 3)
        self.assertNotEqual(
            Task7.character_count('A public service Announcement'
                                  ' followed me', 'n'), 10)

    def test_fizzbuzz(self):
        """Fizzbuzz."""
        self.assertEqual(Task7.fizzbuzz(100), 'Buzz')
        self.assertEqual(Task7.fizzbuzz(1), 1)
