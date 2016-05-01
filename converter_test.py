"""Unit test for conversor.py."""

import unittest
from converter_class import Converter


class ConversorTest(unittest.TestCase):
    """Class ConversorTest."""

    def setUp(self):
        """Arrange context."""
        self.converter = Converter()
        self.decimal = 0

    def test_get_one(self):
        """Test case for number I."""
        self.decimal = self.converter.convert("I")
        self.assertEquals(self.decimal, 1)

    def test_get_two(self):
        """Test case for number II."""
        self.decimal = self.converter.convert("II")
        self.assertEquals(self.decimal, 2)

    def tearDown(self):
        """Destroy context."""
        del(self.converter)
        del(self.decimal)

if __name__ == '__main__':
        unittest.main()
