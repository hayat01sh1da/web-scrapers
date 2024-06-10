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
        self.application = Application()
        self.dirname     = os.path.join('.', 'test', 'tmp')

    def test_webdriver(self):
        if type(self) is TestApplication:
            self.assertEqual("<class 'selenium.webdriver.chrome.webdriver.WebDriver'>", str(type(self.application.chrome)))

    def test_base_url(self):
        if type(self) is TestApplication:
            self.assertEqual('https://scraping-for-beginner.herokuapp.com', self.application.base_url)

    def tearDown(self):
        shutil.rmtree(self.dirname)

if __name__ == '__main__':
    unittest.main()
