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
        self.assertTrue(path.exists(filepath.format(i = 1)))
        self.assertTrue(path.exists(filepath.format(i = 2)))
        self.assertTrue(path.exists(filepath.format(i = 3)))
        self.assertTrue(path.exists(filepath.format(i = 4)))
        self.assertTrue(path.exists(filepath.format(i = 5)))
        self.assertTrue(path.exists(filepath.format(i = 6)))
        self.assertTrue(path.exists(filepath.format(i = 7)))
        self.assertTrue(path.exists(filepath.format(i = 8)))
        self.assertTrue(path.exists(filepath.format(i = 9)))
        self.assertTrue(path.exists(filepath.format(i = 10)))
        self.assertTrue(path.exists(filepath.format(i = 11)))
        self.assertTrue(path.exists(filepath.format(i = 12)))
        self.assertTrue(path.exists(filepath.format(i = 13)))
        self.assertTrue(path.exists(filepath.format(i = 14)))
        self.assertTrue(path.exists(filepath.format(i = 15)))
        self.assertTrue(path.exists(filepath.format(i = 16)))
        self.assertTrue(path.exists(filepath.format(i = 17)))
        self.assertTrue(path.exists(filepath.format(i = 18)))
        self.assertTrue(path.exists(filepath.format(i = 19)))
        self.assertTrue(path.exists(filepath.format(i = 20)))
        self.assertTrue(path.exists(filepath.format(i = 21)))
        self.assertTrue(path.exists(filepath.format(i = 22)))
        self.assertTrue(path.exists(filepath.format(i = 23)))
        self.assertTrue(path.exists(filepath.format(i = 24)))

if __name__ == '__main__':
    unittest.main()
