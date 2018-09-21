from unittest import TestCase

import Task_7


class TestPyTasks(TestCase):

    def setUp(self):
        """SetUp."""

    def test_palindrome(self):
        self.assertFalse(Task_7.ispalindrome('Arina'))
        self.assertTrue(Task_7.ispalindrome('Arinaanira'))

    def test_third_power(self):
        self.assertEqual(Task_7.third_power(6), 216)
        self.assertNotEqual(Task_7.third_power(8), 4096)

    def test_count_characters(self):

        self.assertEqual(
            Task_7.character_count('Home sweet home', 'e'), 4)
        self.assertNotEqual(
            Task_7.character_count('My dear friend', 'd'), 2)

    def test_fizzbuzz(self):
        self.assertEqual(Task_7.fizzbuzz(100), 'Buzz')
        self.assertEqual(Task_7.fizzbuzz(1), 1)
