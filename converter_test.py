"""Unit test for converter_class.py."""

import unittest
from converter_class import Converter


class ConverterTest(unittest.TestCase):
    """Class ConverterTest."""

    def setUp(self):
        """Arrange context."""
        self.converter = Converter()
        self.decimal = 0

    def test_get_one(self):
        """Test case #1: Convert I to decimal 1."""
        self.decimal = self.converter.convert("I")
        self.assertEquals(self.decimal, 1)

    def test_get_two(self):
        """Test case #2: Convert II to decimal 2."""
        self.decimal = self.converter.convert("II")
        self.assertEquals(self.decimal, 2)

    def test_get_three(self):
        """Test case #3: Convert III to decimal 3."""
        self.decimal = self.converter.convert("III")
        self.assertEquals(self.decimal, 3)

    def test_get_four(self):
        """Test case #4: Convert IV to decimal 4."""
        self.decimal = self.converter.convert("IV")
        self.assertEquals(self.decimal, 4)

    def test_get_five(self):
        """Test case #5: Convert V to decimal 5."""
        self.decimal = self.converter.convert("V")
        self.assertEquals(self.decimal, 5)

    def test_get_six(self):
        """Test case #6: Convert VI to decimal 6."""
        self.decimal = self.converter.convert("VI")
        self.assertEquals(self.decimal, 6)

    def test_get_nine(self):
        """Test case #7: Convert IX to decimal 9."""
        self.decimal = self.converter.convert("IX")
        self.assertEquals(self.decimal, 9)

    def test_get_ten(self):
        """Test case #8: Convert X to decimal 10."""
        self.decimal = self.converter.convert("X")
        self.assertEquals(self.decimal, 10)

    def test_get_forty(self):
        """Test case #9: Convert XL to decimal 40."""
        self.decimal = self.converter.convert("XL")
        self.assertEquals(self.decimal, 40)

    def test_get_fifty(self):
        """Test case #10: Convert L to decimal 50."""
        self.decimal = self.converter.convert("L")
        self.assertEquals(self.decimal, 50)

    def test_get_ninety(self):
        """Test case #11: Convert XC to decimal 90."""
        self.decimal = self.converter.convert("XC")
        self.assertEquals(self.decimal, 90)

    def test_get_one_hundred(self):
        """Test case #12: Convert C to decimal 100."""
        self.decimal = self.converter.convert("C")
        self.assertEquals(self.decimal, 100)

    def test_get_four_hundred(self):
        """Test case #13: Convert CD to decimal 400."""
        self.decimal = self.converter.convert("CD")
        self.assertEquals(self.decimal, 400)

    def test_get_five_hundred(self):
        """Test case #14: Convert D to decimal 500."""
        self.decimal = self.converter.convert("D")
        self.assertEquals(self.decimal, 500)

    def test_get_nine_hundred(self):
        """Test case #15: Convert CM to decimal 900."""
        self.decimal = self.converter.convert("CM")
        self.assertEquals(self.decimal, 900)

    def test_get_one_thousand(self):
        """Test case #16: Convert M to decimal 1000."""
        self.decimal = self.converter.convert("M")
        self.assertEquals(self.decimal, 1000)

    def test_get_48(self):
        """Test case #17: Convert XLVIII to decimal 48."""
        self.decimal = self.converter.convert("XLVIII")
        self.assertEquals(self.decimal, 48)

    def test_get_67(self):
        """Test case #18: Convert LXVII to decimal 67."""
        self.decimal = self.converter.convert("LXVII")
        self.assertEquals(self.decimal, 67)

    def test_get_99(self):
        """Test case #19: Convert XCIX to decimal 99."""
        self.decimal = self.converter.convert("XCIX")
        self.assertEquals(self.decimal, 99)

    def test_get_449(self):
        """Test case #20: Convert CDXLIX to decimal 449."""
        self.decimal = self.converter.convert("CDXLIX")
        self.assertEquals(self.decimal, 449)

    def test_get_459(self):
        """Test case #21: Convert CDLIX to decimal 459."""
        self.decimal = self.converter.convert("CDLIX")
        self.assertEquals(self.decimal, 459)

    def test_get_944(self):
        """Test case #22: Convert CMXLIV to decimal 944."""
        self.decimal = self.converter.convert("CMXLIV")
        self.assertEquals(self.decimal, 944)

    def tearDown(self):
        """Destroy context."""
        del(self.converter)
        del(self.decimal)

if __name__ == '__main__':
        unittest.main()
