import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Application:
    def __init__(self, init_webdriver: bool = True):
        """Application core.

        Args:
            init_webdriver: if True, initialize a Selenium Chrome webdriver.
                            Tests may pass False to avoid launching a real
                            browser.
        """
        self.base_url = 'https://scraping-for-beginner.herokuapp.com'
        self.chrome   = None
        if init_webdriver:
            # Initialize webdriver only when requested.
            # Use PATH_TO_WEBDRIVER environment variable to locate the driver service.
            self.chrome = webdriver.Chrome(service = Service(os.environ['PATH_TO_WEBDRIVER']), options = self.__options__())

    # private

    def __options__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        return options
