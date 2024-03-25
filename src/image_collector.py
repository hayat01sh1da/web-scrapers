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
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        self.chrome = webdriver.Chrome(service = Service(os.environ['PATH_TO_WEBDRIVER']), options = options)

    def get_images(self, url):
        self.chrome.get(url)
        img_divs = self.chrome.find_elements(By.CLASS_NAME, 'material-placeholder')
        img_urls = []
        for img_div in img_divs:
            img_urls.append(img_div.find_element(By.TAG_NAME, 'img').get_attribute('src'))
        images = []
        for img_url in img_urls:
            f     = io.BytesIO(request.urlopen(img_url).read())
            image = Image.open(f)
            images.append(image)
        return images

    def save_images(self, images, path):
        i = 1
        for image in images:
            image.save(path.format(i))
            i += 1
