class Converter(object):
    """Class Converter."""

    def __init__(self):
        """Constructor for class Converter."""
        self.romans = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4
        }

    def convert(self, roman):
        """Convert roman numbers to decimal numbers."""
        return self.romans[roman]
