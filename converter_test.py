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

    def test_get_nine(self):
        """Test case for number IX."""
        self.decimal = self.converter.convert("IX")
        self.assertEquals(self.decimal, 9)

    def test_get_ten(self):
        """Test case for number X."""
        self.decimal = self.converter.convert("X")
        self.assertEquals(self.decimal, 10)

    def test_get_forty(self):
        """Test case for number XL."""
        self.decimal = self.converter.convert("XL")
        self.assertEquals(self.decimal, 40)

    def test_get_fifty(self):
        """Test case for number L."""
        self.decimal = self.converter.convert("L")
        self.assertEquals(self.decimal, 50)

    def test_get_ninety(self):
        """Test case for number XC."""
        self.decimal = self.converter.convert("XC")
        self.assertEquals(self.decimal, 90)

    def test_get_one_hundred(self):
        """Test case for number C."""
        self.decimal = self.converter.convert("C")
        self.assertEquals(self.decimal, 100)

    def test_get_four_hundred(self):
        """Test case for number CD."""
        self.decimal = self.converter.convert("CD")
        self.assertEquals(self.decimal, 400)

    def test_get_five_hundred(self):
        """Test case for number D."""
        self.decimal = self.converter.convert("D")
        self.assertEquals(self.decimal, 500)

    def test_get_nine_hundred(self):
        """Test case for number CM."""
        self.decimal = self.converter.convert("CM")
        self.assertEquals(self.decimal, 900)

    def test_get_one_thousand(self):
        """Test case for number M."""
        self.decimal = self.converter.convert("M")
        self.assertEquals(self.decimal, 1000)

    def tearDown(self):
        """Destroy context."""
        del(self.converter)
        del(self.decimal)

if __name__ == '__main__':
        unittest.main()
