import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_word(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test_english_to_french_null(self):
        self.assertNotEqual(english_to_french('None'),'')
       
    def test_french_to_english_word(self):
        self.assertNotEqual(french_to_english('None'),'')
    def test_french_to_english_null(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")


unittest.main()