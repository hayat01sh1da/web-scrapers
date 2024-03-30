import unittest
import os
import sys
sys.path.append('./src')
sys.path.append('./test')
from os import path
from image_collector import ImageCollector
from test_application import TestApplication

class TestImageCollector(TestApplication):
    def setUp(self):
        super().setUp()
        self.image_collector = ImageCollector()
        self.filename        = 'image_{i:02}.jpg'

    def test_save_images(self):
        self.image_collector.save_images(self.dirname, self.filename)
        filepath = os.path.join(self.dirname, self.filename)
        self.assertEqual(True, path.exists(filepath.format(i = 1)))
        self.assertEqual(True, path.exists(filepath.format(i = 2)))
        self.assertEqual(True, path.exists(filepath.format(i = 3)))
        self.assertEqual(True, path.exists(filepath.format(i = 4)))
        self.assertEqual(True, path.exists(filepath.format(i = 5)))
        self.assertEqual(True, path.exists(filepath.format(i = 6)))
        self.assertEqual(True, path.exists(filepath.format(i = 7)))
        self.assertEqual(True, path.exists(filepath.format(i = 8)))
        self.assertEqual(True, path.exists(filepath.format(i = 9)))
        self.assertEqual(True, path.exists(filepath.format(i = 10)))
        self.assertEqual(True, path.exists(filepath.format(i = 11)))
        self.assertEqual(True, path.exists(filepath.format(i = 12)))
        self.assertEqual(True, path.exists(filepath.format(i = 13)))
        self.assertEqual(True, path.exists(filepath.format(i = 14)))
        self.assertEqual(True, path.exists(filepath.format(i = 15)))
        self.assertEqual(True, path.exists(filepath.format(i = 16)))
        self.assertEqual(True, path.exists(filepath.format(i = 17)))
        self.assertEqual(True, path.exists(filepath.format(i = 18)))
        self.assertEqual(True, path.exists(filepath.format(i = 19)))
        self.assertEqual(True, path.exists(filepath.format(i = 20)))
        self.assertEqual(True, path.exists(filepath.format(i = 21)))
        self.assertEqual(True, path.exists(filepath.format(i = 22)))
        self.assertEqual(True, path.exists(filepath.format(i = 23)))
        self.assertEqual(True, path.exists(filepath.format(i = 24)))

if __name__ == '__main__':
    unittest.main()
