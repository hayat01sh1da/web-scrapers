import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Application:
    def __init__(self):
        self.chrome    = webdriver.Chrome(service = Service(os.environ['PATH_TO_WEBDRIVER']), options = self.__options__())
        self.base_url  = 'https://scraping-for-beginner.herokuapp.com'

    # private

    def __options__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        return options
