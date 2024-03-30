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
        self.assertEqual("<class 'selenium.webdriver.chrome.webdriver.WebDriver'>", str(type(self.application.chrome)))

    def test_base_url(self):
        self.assertEqual('https://scraping-for-beginner.herokuapp.com', self.application.base_url)

    def tearDown(self):
        if self.__has_json_file__():
            shutil.rmtree(self.dirname)

    # private

    def __has_json_file__(self):
        return len(glob.glob(os.path.join(self.dirname, '*'))) >= 1

if __name__ == '__main__':
    unittest.main()
