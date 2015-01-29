import unittest
import conversion


class conversionTest(unittest.TestCase):

    def test_arabic_to_roman_invalid_type(self):
        self.assertRaises(ValueError, conversion.Conversion.arabic_to_roman,
                          "Hello")

    def test_arabic_to_roman_zero(self):
        self.assertRaises(ValueError, conversion.Conversion.arabic_to_roman, 0)

    def test_arabic_to_roman_negative_number_with_negatives_false(self):
        self.assertRaises(ValueError,
                          conversion.Conversion.arabic_to_roman, -15)

    def test_arabic_to_roman_greater_than_max(self):
        self.assertRaises(ValueError, conversion.Conversion.arabic_to_roman,
                          conversion.Conversion.max_arab_to_rom+1)

    def test_arabic_to_roman_floating_point_number(self):
        self.assertEqual("XXI", conversion.Conversion.arabic_to_roman(21.15))

    def test_arabic_to_roman_int_floating_point_number(self):
        self.assertEqual("XXI", conversion.Conversion.arabic_to_roman(21.0))

    def test_arabic_to_roman_one(self):
        self.assertEqual("XXI", conversion.Conversion.arabic_to_roman(21.0))

    def test_arabic_to_roman_three_thousand_nine_hundred_ninety_nine(self):
        self.assertEqual("MMMCMXCIX",
                         conversion.Conversion.arabic_to_roman(3999))

    def test_arabic_to_roman_four(self):
        self.assertEqual("IV", conversion.Conversion.arabic_to_roman(4))

    def test_arabic_to_roman_five_hundred_seventy_eight(self):
        self.assertEqual("DLXXVIII",
                         conversion.Conversion.arabic_to_roman(578))

    def test_arabic_to_roman_two(self):
        self.assertEqual("II", conversion.Conversion.arabic_to_roman(2))

    def test_arabic_to_roman_thirteen(self):
        self.assertEqual("XIII", conversion.Conversion.arabic_to_roman(13))

    def test_arabic_to_roman_two_hundred_seven(self):
        self.assertEqual("CCVII", conversion.Conversion.arabic_to_roman(207))

    def test_arabic_to_roman_one_thousand_sixty_six(self):
        self.assertEqual("MLXVI", conversion.Conversion.arabic_to_roman(1066))

    def test_arabic_to_roman_one_thousand_nine_hundred_fifty_four(self):
        self.assertEqual("MCMLIV", conversion.Conversion.arabic_to_roman(1954))

    def test_arabic_to_roman_two_thousand_nine_hundred_ninety(self):
        self.assertEqual("MMCMXC", conversion.Conversion.arabic_to_roman(2990))

    def test_arabic_to_roman_two_thousand_fourteen(self):
        self.assertEqual("MMXIV", conversion.Conversion.arabic_to_roman(2014))

    def test_arabic_to_roman_eighty_seven(self):
        self.assertEqual("LXXXVII", conversion.Conversion.arabic_to_roman(87))

    def test_arabic_to_roman_lower_than_min_negatives_true(self):
        self.assertRaises(ValueError, conversion.Conversion.arabic_to_roman,
                          0 - (conversion.Conversion.max_arab_to_rom+1), True)

    def test_arabic_to_roman_floating_point_number_neg(self):
        self.assertEqual("-XXI",
                         conversion.Conversion.arabic_to_roman(-21.15, True))

    def test_arabic_to_roman_int_floating_point_number_neg(self):
        self.assertEqual("-XXI",
                         conversion.Conversion.arabic_to_roman(-21.0, True))

    def test_arabic_to_roman_one_neg(self):
        self.assertEqual("-XXI",
                         conversion.Conversion.arabic_to_roman(-21.0, True))

    def test_arabic_to_roman_three_thousand_nine_hundred_ninety_nine_neg(self):
        self.assertEqual("-MMMCMXCIX",
                         conversion.Conversion.arabic_to_roman(-3999, True))

    def test_arabic_to_roman_four_neg(self):
        self.assertEqual("-IV",
                         conversion.Conversion.arabic_to_roman(-4, True))

    def test_arabic_to_roman_five_hundred_seventy_eight_neg(self):
        self.assertEqual("-DLXXVIII",
                         conversion.Conversion.arabic_to_roman(-578, True))

    def test_arabic_to_roman_two_neg(self):
        self.assertEqual("-II",
                         conversion.Conversion.arabic_to_roman(-2, True))

    def test_arabic_to_roman_thirteen_neg(self):
        self.assertEqual("-XIII",
                         conversion.Conversion.arabic_to_roman(-13, True))

    def test_arabic_to_roman_two_hundred_seven_neg(self):
        self.assertEqual("-CCVII",
                         conversion.Conversion.arabic_to_roman(-207, True))

    def test_arabic_to_roman_one_thousand_sixty_six_neg(self):
        self.assertEqual("-MLXVI",
                         conversion.Conversion.arabic_to_roman(-1066, True))

    def test_arabic_to_roman_one_thousand_nine_hundred_fifty_four_neg(self):
        self.assertEqual("-MCMLIV",
                         conversion.Conversion.arabic_to_roman(-1954, True))

    def test_arabic_to_roman_two_thousand_nine_hundred_ninety_neg(self):
        self.assertEqual("-MMCMXC",
                         conversion.Conversion.arabic_to_roman(-2990, True))

    def test_arabic_to_roman_two_thousand_fourteen_neg(self):
        self.assertEqual("-MMXIV",
                         conversion.Conversion.arabic_to_roman(-2014, True))

    def test_arabic_to_roman_eighty_seven_neg(self):
        self.assertEqual("-LXXXVII",
                         conversion.Conversion.arabic_to_roman(-87, True))

if __name__ == "__main__":
    unittest.main()
