class Conversion:

    def __init__(self):
        # Order matters, so a dictionary would not be the best choice.
        # We don't want to run the risk of having the values changed in place,
        # hence the choice of using tuple rather than list.
        self.std_romans = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                           (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                           (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

        # To increase the range of coverage, simply add the values with their
        # representation to the 'self.std.romans' tuple and update
        # 'self.max_rom_to_arab' accordingly.
        self.max_rom_to_arab = 3999

    def arabic_to_roman(self, arabic):
        # Validations:
        # The passed parameter must be an integer.
        # Integer must be positive between 1 and 3999.
        value = int(arabic)

        if value <= 0 or value > self.max_rom_to_arab:
            raise ValueError("Value must be an integer between 1 and %d"
                             % self.max_rom_to_arab)
        else:
            res = []
            for arab, rom in self.std_romans:
                times = value//arab
                if times:
                    for i in range(times):
                        res.append(rom)
                value -= times*arab
            return "".join(res)


if __name__ == "__main__":
    conv = Conversion()
    for i in range(1, 4000):
        print i, conv.arabic_to_roman(i)

    print 4000, conv.arabic_to_roman(4000)
