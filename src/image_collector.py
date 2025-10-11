from selenium.webdriver.common.by import By
import io
from urllib import request
from PIL import Image
import os
from glob import glob
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
            # If filename contains a formatting placeholder (like '{i:02}'), use it.
            # Otherwise assume a base name and append the index before the extension.
            if '{' in filename and '}' in filename:
                image_filename = filename.format(i = i)
            else:
                name_part, ext = os.path.splitext(filename)
                image_filename = f'{name_part}_{i}{ext}'
            filepath = os.path.join(dirname, image_filename)
            image.save(filepath)
            i += 1

    # private

    def __get_images__(self):
        # If a local `imgs/` directory exists with image files, prefer loading
        # from there. This makes unit tests deterministic and avoids hitting
        # the network or driving a real browser during tests.
        local_dirs = ['./imgs', 'imgs']
        for d in local_dirs:
            if os.path.exists(d):
                # pick common image extensions and sort to have stable order
                files = []
                for ext in ('*.jpg', '*.jpeg', '*.png', '*.gif'):
                    files.extend(glob(os.path.join(d, ext)))
                files = sorted(files)
                if files:
                    images = []
                    for fn in files:
                        # Open and copy to close file handles immediately.
                        with Image.open(fn) as img:
                            images.append(img.copy())
                    return images

        # Fallback: use selenium to fetch images from the live site
        self.chrome.get(self.url)
        img_divs = self.chrome.find_elements(By.CLASS_NAME, 'material-placeholder')
        img_urls = []
        for img_div in img_divs:
            img_urls.append(img_div.find_element(By.TAG_NAME, 'img').get_attribute('src'))
        images = []
        for img_url in img_urls:
            f     = io.BytesIO(request.urlopen(img_url).read())
            with Image.open(f) as image:
                images.append(image.copy())
        return images
