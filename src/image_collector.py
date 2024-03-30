from selenium.webdriver.common.by import By
import io
from urllib import request
from PIL import Image
import os
from application import Application

class ImageCollector(Application):
    def __init__(self):
        super().__init__()
        self.url = '{base_url}/{path}'.format(base_url = self.base_url, path = 'image')

    def save_images(self, dirname, filename):
        if not os.path.isdir(dirname):
            os.makedirs(dirname)

        filepath = os.path.join(dirname, filename)
        i        = 1
        for image in self.__get_images__():
            image.save(filepath.format(i = i))
            i += 1

    # private

    def __get_images__(self):
        self.chrome.get(self.url)
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
