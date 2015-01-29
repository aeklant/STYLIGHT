"""
This module is intended to be used as a library to store different types of
common-place conversions such as converting an Arabic numeral to its Roman
numeral representation.
"""


class Conversion(object):
    """
    The purpose of this class is to provide an easy way to extend the
    conversions library in the future.

    Rules:
    - There is no roman representation for the number 0 (zero).
    - No roman character can appear more than 3 consecutive times.
    - The maximum representable number is constrained by the set of roman
      characters and the previous rule (Here the maximum is 3999, although it
      can be easily increased by providing more roman characters).
    """

    # Order matters, so a dictionary would not be the best choice.
    # We don't want to run the risk of having the values changed in place,
    # hence the choice of using tuple rather than list.
    std_romans = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                  (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                  (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

    # To increase the range of coverage, simply add the values with their
    # representation to the 'std.romans' tuple and update
    # 'max_rom_to_arab' accordingly.
    max_rom_to_arab = 3999

    @staticmethod
    def arabic_to_roman(arabic, negatives=False):
        """
        Static method. Receives an arabic numeral and returns the roman
        representation for said numeral.

        If the value to be converted does not have an integer representation,
        the value is 0 (zero) or the value is beyond range a ValueError
        exception is raised. If the value is a floationg point number, it is
        truncated to its integer value (e.g. 3.141592 is taken as 3).

        Default range is from 1 to max_rom_to_arab. If 'negatives' is set to
        True the range is increased to include negative numbers from -1 to
        negative 'max_rom_to_arab'.
        """
        try:
            value = int(arabic)
        except ValueError:
            raise ValueError("The value must be a number")
        res = []

        if value < 0:
            if negatives:
                if abs(value) <= 3999:
                    res.append("-")
                    value = abs(value)
                else:
                    mess = ("The number's absolute value must be %d or lower"
                            % Conversion.max_rom_to_arab)

                    raise ValueError(mess)
            else:
                raise ValueError("Negatives not supported by default, try using"
                                 + " 'negatives=True' as a parameter")

        if value == 0 or value > Conversion.max_rom_to_arab:
            raise ValueError("Value must be an integer between 1 and %d"
                             % Conversion.max_rom_to_arab)
        else:
            for arab, rom in Conversion.std_romans:
                times = value//arab     # For 2.X, 3.X compatibility
                if times:
                    for i in range(times):
                        res.append(rom)
                value -= times*arab
            return "".join(res)
