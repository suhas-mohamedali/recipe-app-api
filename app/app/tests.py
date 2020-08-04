from django.test import TestCase

from app.calc import add, substract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """Test Adding two numbers"""
        self.assertEqual(add(3, 8), 11)

    def test_substract(self):
        """Test sunstraction"""
        self.assertEqual(substract(5, 11), 6)
