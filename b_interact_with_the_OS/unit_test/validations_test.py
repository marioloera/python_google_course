import unittest
from validations import validate_user


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user('validuser', 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user('validuser', 30), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user('invalid_user', 3), False)

    def test_invalid_minlen(self):
        # parameters
        # error rais expected to be raised
        # function name
        # functions parameters
        self.assertRaises(ValueError, validate_user, 'validuser', -3)

unittest.main()