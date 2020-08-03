from django.test import TestCase

from app.calc import add


class CalcTest(TestCase):
    def test_add_numbers(self):
        """Test Adding two numbers"""
        self.assertEqual(add(3, 8), 11)
