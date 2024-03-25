from selenium.webdriver.common.by import By
import io
from urllib import request
from PIL import Image
import sys
sys.path.append('./src/lib')
from chrome_driver import ChromeDriver

class ImageCollector:
    def __init__(self):
        self.chrome = ChromeDriver().webdriver

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
