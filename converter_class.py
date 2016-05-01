class Converter(object):
    """Class Converter."""

    def __init__(self):
        """Constructor for class Converter."""
        self.bufferedRoman = str()
        self.romanNumerals = [("IX", 9), ("IV", 4), ("V", 5), ("I", 1)]

    def convert(self, roman):
        """Convert roman numbers to decimal numbers."""
        self.bufferedRoman = roman
        convertedNumber = 0
        maximum = self.getMaximumNumeral()

        while maximum:
            convertedNumber += maximum
            maximum = self.getMaximumNumeral()

        return convertedNumber

    def getMaximumNumeral(self):
        """Return maximum digit in a roman number."""
        if not self.bufferedRoman:
            return 0

        for (numeral, value) in self.romanNumerals:
            if numeral in self.bufferedRoman:
                self.bufferedRoman = self.bufferedRoman.replace(numeral, "", 1)
                return value
