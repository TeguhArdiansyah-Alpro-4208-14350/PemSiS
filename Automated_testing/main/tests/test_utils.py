from django.test import TestCase
from main.utils import calculator, validate_password

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(calculator(2, 3, '+'), 5)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculator(1, 2, '%')

class PasswordValidationTest(TestCase):
    def test_valid_password(self):
        self.assertTrue(validate_password("Aman123!"))
    
    def test_invalid_short(self):
        self.assertFalse(validate_password("a1A!"))
