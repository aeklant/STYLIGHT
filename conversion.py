class Conversion:

    def __init__(self):
        self.std_romans = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C",
                           500: "D", 1000: "M"}
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
            return "".join(res)
