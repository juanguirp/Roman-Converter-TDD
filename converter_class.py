import collections


class Converter(object):
    """Class Converter."""

    def __init__(self):
        """Constructor for class Converter."""
        self.bufferedRoman = str()
        self.romanNumerals = {
            "IV": 4,
            "I": 1
        }

    def convert(self, roman):
        """Convert roman numbers to decimal numbers."""
        self.bufferedRoman = roman
        convertedNumber = 0
        maximum = self.getMaximumDigit()
        while maximum:
            convertedNumber += maximum
            maximum = self.getMaximumDigit()
        return convertedNumber

    def getMaximumDigit(self):
        """Return maximum digit in a roman number."""
        if not self.bufferedRoman:
            return 0

        for numeral, value in sorted(self.romanNumerals.iteritems(), key=lambda (k, v): (v, k), reverse=True):
            if numeral in self.bufferedRoman:
                self.bufferedRoman = self.bufferedRoman.replace(numeral, "", 1)
                return value
