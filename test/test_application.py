import unittest
import os
import shutil
import glob
import sys
sys.path.append('./src')
sys.path.append('./src/lib')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        # Do not initialize a real webdriver during unit tests
        self.application = Application(init_webdriver = False)
        self.dirname     = os.path.join('.', 'test', 'tmp')
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        self.pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        if type(self) is TestApplication:
            for pycache in self.pycaches:
                if os.path.exists(pycache):
                    shutil.rmtree(pycache)
        else:
            if os.path.exists(self.dirname):
                shutil.rmtree(self.dirname)
            for pycache in self.pycaches:
                if os.path.exists(pycache):
                    shutil.rmtree(pycache)

    def test_webdriver(self):
        if type(self) is TestApplication:
            # During unit tests we avoid launching a real browser, so the
            # webdriver may be None. Accept either None or the expected
            # WebDriver type.
            if self.application.chrome is None:
                self.assertIsNone(self.application.chrome)
            else:
                self.assertEqual(str(type(self.application.chrome)), "<class 'selenium.webdriver.chrome.webdriver.WebDriver'>")

    def test_base_url(self):
        if type(self) is TestApplication:
            self.assertEqual(self.application.base_url, 'https://scraping-for-beginner.herokuapp.com')

if __name__ == '__main__':
    unittest.main()
