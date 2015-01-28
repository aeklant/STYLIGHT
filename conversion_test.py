import unittest
import conversion


class conversionTest(unittest.TestCase):
    conv = conversion.Conversion()

    def test_arabic_to_roman_invalid_type(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman,
                          "Hello")

    def test_arabic_to_roman_negative_number(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman, -15)

    def test_arabic_to_roman_zero(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman, 0)

    def test_arabic_to_roman_greater_than_max(self):
        self.assertRaises(ValueError, conversionTest.conv.arabic_to_roman,
                          conversionTest.conv.max_rom_to_arab+1)

    def test_arabic_to_roman_floating_point_number(self):
        self.assertEqual("XXI", conversionTest.conv.arabic_to_roman(21.15))

    def test_arabic_to_roman_int_floating_point_number(self):
        self.assertEqual("XXI", conversionTest.conv.arabic_to_roman(21.0))

    def test_arabic_to_roman_one(self):
        self.assertEqual("XXI", conversionTest.conv.arabic_to_roman(21.0))

if __name__ == "__main__":
    unittest.main()
