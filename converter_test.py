"""Unit test for conversor.py."""

import unittest
from converter_class import Converter


class ConversorTest(unittest.TestCase):
    """Class ConversorTest."""

    def test_get_one(self):
        """Test case for number I."""
        converter = Converter()
        decimal = 0
        decimal = converter.convert("I")
        self.assertEquals(decimal, 1)

    def test_get_two(self):
        """Test case for number II."""
        converter = Converter()
        decimal = 0
        decimal = converter.convert("II")
        self.assertEquals(decimal, 2)

if __name__ == '__main__':
        unittest.main()
