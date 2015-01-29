import unittest
import conversion


class conversionTest(unittest.TestCase):
    conv = conversion.Conversion()

    def test_arabic_to_roman_invalid_type(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman,
                          "Hello")

    def test_arabic_to_roman_zero(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman, 0)

    def test_arabic_to_roman_negative_number_with_negatives_false(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman, -15)

    def test_arabic_to_roman_greater_than_max(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman,
                          conversionTest.conv.max_rom_to_arab+1)

    def test_arabic_to_roman_floating_point_number(self):
        self.assertEqual("XXI", conversionTest.conv.arabic_to_roman(21.15))

    def test_arabic_to_roman_int_floating_point_number(self):
        self.assertEqual("XXI", conversionTest.conv.arabic_to_roman(21.0))

    def test_arabic_to_roman_one(self):
        self.assertEqual("XXI", conversionTest.conv.arabic_to_roman(21.0))

    def test_arabic_to_roman_three_thousand_nine_hundred_ninety_nine(self):
        self.assertEqual("MMMCMXCIX",
                         conversionTest.conv.arabic_to_roman(3999))

    def test_arabic_to_roman_four(self):
        self.assertEqual("IV", conversionTest.conv.arabic_to_roman(4))

    def test_arabic_to_roman_five_hundred_seventy_eight(self):
        self.assertEqual("DLXXVIII", conversionTest.conv.arabic_to_roman(578))

    def test_arabic_to_roman_two(self):
        self.assertEqual("II", conversionTest.conv.arabic_to_roman(2))

    def test_arabic_to_roman_thirteen(self):
        self.assertEqual("XIII", conversionTest.conv.arabic_to_roman(13))

    def test_arabic_to_roman_two_hundred_seven(self):
        self.assertEqual("CCVII", conversionTest.conv.arabic_to_roman(207))

    def test_arabic_to_roman_one_thousand_sixty_six(self):
        self.assertEqual("MLXVI", conversionTest.conv.arabic_to_roman(1066))

    def test_arabic_to_roman_one_thousand_nine_hundred_fifty_four(self):
        self.assertEqual("MCMLIV", conversionTest.conv.arabic_to_roman(1954))

    def test_arabic_to_roman_two_thousand_nine_hundred_ninety(self):
        self.assertEqual("MMCMXC", conversionTest.conv.arabic_to_roman(2990))

    def test_arabic_to_roman_two_thousand_fourteen(self):
        self.assertEqual("MMXIV", conversionTest.conv.arabic_to_roman(2014))

    def test_arabic_to_roman_eighty_seven(self):
        self.assertEqual("LXXXVII", conversionTest.conv.arabic_to_roman(87))

    def test_arabic_to_roman_lower_than_min_negatives_true(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman,
                          0 - (conversionTest.conv.max_rom_to_arab+1), True)

    def test_arabic_to_roman_floating_point_number_neg(self):
        self.assertEqual("-XXI",
                         conversionTest.conv.arabic_to_roman(-21.15, True))

    def test_arabic_to_roman_int_floating_point_number_neg(self):
        self.assertEqual("-XXI",
                         conversionTest.conv.arabic_to_roman(-21.0, True))

    def test_arabic_to_roman_one_neg(self):
        self.assertEqual("-XXI",
                         conversionTest.conv.arabic_to_roman(-21.0, True))

    def test_arabic_to_roman_three_thousand_nine_hundred_ninety_nine_neg(self):
        self.assertEqual("-MMMCMXCIX",
                         conversionTest.conv.arabic_to_roman(-3999, True))

    def test_arabic_to_roman_four_neg(self):
        self.assertEqual("-IV", conversionTest.conv.arabic_to_roman(-4, True))

    def test_arabic_to_roman_five_hundred_seventy_eight_neg(self):
        self.assertEqual("-DLXXVIII",
                         conversionTest.conv.arabic_to_roman(-578, True))

    def test_arabic_to_roman_two_neg(self):
        self.assertEqual("-II", conversionTest.conv.arabic_to_roman(-2, True))

    def test_arabic_to_roman_thirteen_neg(self):
        self.assertEqual("-XIII",
                         conversionTest.conv.arabic_to_roman(-13, True))

    def test_arabic_to_roman_two_hundred_seven_neg(self):
        self.assertEqual("-CCVII",
                         conversionTest.conv.arabic_to_roman(-207, True))

    def test_arabic_to_roman_one_thousand_sixty_six_neg(self):
        self.assertEqual("-MLXVI",
                         conversionTest.conv.arabic_to_roman(-1066, True))

    def test_arabic_to_roman_one_thousand_nine_hundred_fifty_four_neg(self):
        self.assertEqual("-MCMLIV",
                         conversionTest.conv.arabic_to_roman(-1954, True))

    def test_arabic_to_roman_two_thousand_nine_hundred_ninety_neg(self):
        self.assertEqual("-MMCMXC",
                         conversionTest.conv.arabic_to_roman(-2990, True))

    def test_arabic_to_roman_two_thousand_fourteen_neg(self):
        self.assertEqual("-MMXIV",
                         conversionTest.conv.arabic_to_roman(-2014, True))

    def test_arabic_to_roman_eighty_seven_neg(self):
        self.assertEqual("-LXXXVII",
                         conversionTest.conv.arabic_to_roman(-87, True))

if __name__ == "__main__":
    unittest.main()
