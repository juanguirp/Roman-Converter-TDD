"""Unit test for conversor.py."""

import unittest
from converter_class import Converter


class ConversorTest(unittest.TestCase):
    """Class ConversorTest."""

    def test_get_one(self):
        """Test case for numer I."""
        converter = Converter()
        decimal = 0
        decimal = converter.convert("I")
        self.assertEquals(decimal, 1)

if __name__ == '__main__':
        unittest.main()
