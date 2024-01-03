"""
sample tests
"""
from django.test import SimpleTestCase


from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(1, 2)

        self.assertEqual(res, 3)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(4, 7)

        self.assertEqual(res, 3)