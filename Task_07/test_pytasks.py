"""Unit tests"""

import pytasks
import unittest


class TestPytasks(unittest.TestCase):
    """Unit tests for pytasks.py"""
    def setUp(self):
        """Init"""

    def test_generate_numbers(self):
        """Test generate_numbers()"""
        self.assertEqual(pytasks.generate_numbers(3), {1: 1, 2: 4, 3: 9})

    def test_count_characters(self):
        """Test count_characters()"""
        self.assertEqual(pytasks.count_characters('qwertyqq'),
                         {'q': 3, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1})

    def test_is_palindrome(self):
        """Test is_palindrome"""
        self.assertTrue(pytasks.is_palindrome('1221'))
        self.assertFalse(pytasks.is_palindrome('efvere'))
