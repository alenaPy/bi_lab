from unittest import TestCase
import prime

class TestPrime(TestCase):

  def setUp(self):
    """Init"""

  def test_is_prime(self):
    """Test for is _prime"""
    self.assertFalse(prime.is_prime(4))
    self.assertTrue(prime.is_prime(13))

  def test_print_next_prime(self):
    self.assertEqual(prime.print_next_prime(9), 11)


  def tearDown(self):
    """Finish"""
