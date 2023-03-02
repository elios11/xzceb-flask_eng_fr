import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english
            ("J'adore les croissants!"), "I love croissants!"
        )
        self.assertNotEqual(french_to_english
            ("J'adore les croissants!"), "J'adore les croissants!"
        )
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english(""))

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french
            ("I'm Zack, nice to meet you!"), "Je suis Zack, sympa de te rencontrer !"
        )
        self.assertNotEqual(english_to_french
            ("I'm Zack, nice to meet you!"), "I'm Zack, nice to meet you!"
        )
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french(""))

unittest.main()