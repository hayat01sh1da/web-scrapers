import unittest
import os
import sys
sys.path.append('./src')
from os import path
from text_extractor import TextExtractor
from test_application import TestApplication

class TestTextExtractor(TestApplication):
    def setUp(self):
        super().setUp()
        self.text_extractor = TextExtractor()
        self.text_extractor.login('imanishi', 'kohei')
        self.filename = 'lecturer_info.csv'

    def test_get_lecturer_info(self):
        profile, *_ = self.text_extractor.get_lecturer_info()
        self.assertEqual({
            '講師名': '今西 航平',
            '所属企業': '株式会社キカガク',
            '生年月日': '1994年7月15日',
            '出身': '千葉県',
            '趣味': 'バスケットボール、読書、ガジェット集め'
        }, profile)

    def test_export_csv(self):
        _, keys, vals = self.text_extractor.get_lecturer_info()
        self.text_extractor.export_csv(keys, vals, self.dirname, self.filename)
        self.assertEqual(True, path.exists(os.path.join(self.dirname, self.filename)))

if __name__ == '__main__':
    unittest.main()
