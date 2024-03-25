import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ChromeDriver:
    def __init__(self):
        self.webdriver = webdriver.Chrome(service = Service(os.environ['PATH_TO_WEBDRIVER']), options = self.__options__())

    # private

    def __options__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        return options
