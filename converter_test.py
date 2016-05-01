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

    def test_get_three(self):
        """Test case for number III."""
        self.decimal = self.converter.convert("III")
        self.assertEquals(self.decimal, 3)

    def test_get_four(self):
        """Test case for number IV."""
        self.decimal = self.converter.convert("IV")
        self.assertEquals(self.decimal, 4)

    def test_get_five(self):
        """Test case for number V."""
        self.decimal = self.converter.convert("V")
        self.assertEquals(self.decimal, 5)

    def test_get_six(self):
        """Test case for number VI."""
        self.decimal = self.converter.convert("VI")
        self.assertEquals(self.decimal, 6)

    def tearDown(self):
        """Destroy context."""
        del(self.converter)
        del(self.decimal)

if __name__ == '__main__':
        unittest.main()
