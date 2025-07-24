import unittest
import sys
sys.path.append('./src')
sys.path.append('./test')
from os import path
from pillow_sample import PillowSample
from test_application import TestApplication

class TestPillowSample(TestApplication):
    def setUp(self):
        super().setUp()
        self.filename      = 'bird{suffix}.jpg'
        self.filepath      = '{dirname}/{filename}'
        self.pillow_sample = PillowSample(self.filepath.format(dirname = './imgs', filename = self.filename.format(suffix = '')))

    def test_image_size(self):
        self.assertEqual(self.pillow_sample.image.size, (1200, 798))

    def test_resize_image(self):
        self.assertEqual(self.pillow_sample.resize_image((1024, 768)), (1024, 768))

    def test_save_image(self):
        self.pillow_sample.resize_image((1024, 768))
        filepath = self.filepath.format(dirname = self.dirname, filename = self.filename.format(suffix = '_resized'))
        self.pillow_sample.save_image(self.dirname, self.filename.format(suffix = '_resized'))
        self.assertTrue(path.exists(filepath))

if __name__ == '__main__':
    unittest.main()
