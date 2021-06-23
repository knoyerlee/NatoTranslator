import unittest
from translator import NATOTranslator as nt

class NatoTesting(unittest.TestCase):
    def setUp(self):
        self.user_letter = 'a'
        self.translator =  nt()

    def test_translate_letter(self):
       translated_letter = self.translator.translate_letter(self.user_letter)
       self.assertEquals(translated_letter, 'Alpha')

if __name__ == '__main__':
    unittest.main()