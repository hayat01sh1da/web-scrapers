import unittest
import sys
sys.path.append('./src')
sys.path.append('./imgs')
from os import path
from image_collector import ImageCollector

class TestImageCollector(unittest.TestCase):
    def setUp(self):
        self.image_collector = ImageCollector()
        self.url             = 'https://scraping-for-beginner.herokuapp.com/image'

    def test_get_images(self):
        self.assertEqual(24, len(self.image_collector.get_images(self.url)))

    def test_save_images(self):
        images = self.image_collector.get_images(self.url)
        self.image_collector.save_images(images, './imgs/image_{:0=2}.jpg')
        self.assertEqual(True, path.exists('./imgs/image_01.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_02.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_03.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_04.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_05.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_06.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_07.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_08.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_09.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_10.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_11.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_12.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_13.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_14.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_15.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_16.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_17.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_18.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_19.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_20.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_21.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_22.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_23.jpg'))
        self.assertEqual(True, path.exists('./imgs/image_24.jpg'))

if __name__ == '__main__':
    unittest.main()
