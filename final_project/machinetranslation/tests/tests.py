import unittest

from translator import englishToFrench, frenchToEnglish

class TestEtoF(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(englishToFrench(""), "")

    def test_single_word(self):
        self.assertEqual(englishToFrench("Strawberry"), "Fraise")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    
    def test_sentence(self):
        self.assertEqual(englishToFrench("Hello, my name is John"), "Bonjour, mon nom est John")
    
    def test_null(self):
        self.assertRaises(ValueError, englishToFrench, None)

class TestFtoE(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(frenchToEnglish(""), "")

    def test_single_word(self):
        self.assertEqual(frenchToEnglish("Fraise"), "Strawberry")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    
    def test_sentence(self):
        self.assertEqual(frenchToEnglish("Bonjour, mon nom est John"), "Hello, my name is John")
    
    def test_null(self):
        self.assertRaises(ValueError, frenchToEnglish, None)
