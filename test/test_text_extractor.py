import unittest
import os
import csv
import sys
sys.path.append('./src')
from os import path
from text_extractor import TextExtractor
from test_application import TestApplication

class TestTextExtractor(TestApplication):
    def setUp(self):
        super().setUp()
        self.text_extractor = TextExtractor(init_webdriver = False)
        # login() will be a no-op in tests because webdriver is disabled,
        # but keep the call to mirror real usage.
        self.text_extractor.login('imanishi', 'kohei')
        self.filename = 'lecturer_info.csv'

    def test_save_csv(self):
        self.text_extractor.save_csv(self.dirname, self.filename)
        filepath      = os.path.join(os.path.join(self.dirname, self.filename))
        lecturer_info = []
        with open(filepath) as f:
            items = csv.DictReader(f)
            for item in items:
                lecturer_info.append(item)
        self.assertTrue(path.exists(filepath))
        self.assertEqual(
            lecturer_info,
            [
                {'': '0', '項目': '講師名', '値': '今西 航平'},
                {'': '1', '項目': '所属企業', '値': '株式会社キカガク'},
                {'': '2', '項目': '生年月日', '値': '1994年7月15日'},
                {'': '3', '項目': '出身', '値': '千葉県'},
                {'': '4', '項目': '趣味', '値': 'バスケットボール、読書、ガジェット集め'}
            ]
        )

if __name__ == '__main__':
    unittest.main()
