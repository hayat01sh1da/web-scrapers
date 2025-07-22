from selenium.webdriver.common.by import By
import io
from urllib import request
from PIL import Image
import os
from application import Application

class ImageCollector(Application):
    def __init__(self):
        super().__init__()
        self.url = f'{self.base_url}/image'

    def save_images(self, dirname, filename):
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        i = 1
        for image in self.__get_images__():
            # Assume filename has an extension, insert number before the extension
            name_part, ext = os.path.splitext(filename)
            image_filename = f'{name_part}_{i}{ext}'
            filepath = os.path.join(dirname, image_filename)
            image.save(filepath)
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
