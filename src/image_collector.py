import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import io
from urllib import request
from PIL import Image
import sys
sys.path.append('./imgs')

class ImageCollector:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        self.chrome = webdriver.Chrome(service=Service(os.environ['PATH_TO_WEBDRIVER']), options=options)
        self.chrome.get(url)
        self.images = None

    def get_images(self):
        img_divs = self.chrome.find_elements(By.CLASS_NAME, 'material-placeholder')
        img_urls = []
        for img_div in img_divs:
            img_urls.append(img_div.find_element(By.TAG_NAME, 'img').get_attribute('src'))
        self.images = []
        for img_url in img_urls:
            f = io.BytesIO(request.urlopen(img_url).read())
            image = Image.open(f)
            self.images.append(image)
        return self.images

    def save_images(self, path):
        i = 1
        for image in self.images:
            image.save(path.format(i))
            i += 1
