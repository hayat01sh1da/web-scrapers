from PIL import Image
import os
import sys
sys.path.append('./src')
from application import Application

class PillowSample(Application):
    def __init__(self, filepath):
        super().__init__()
        self.image = Image.open(filepath)

    def resize_image(self, size):
        return self.image.resize(size).size

    def save_image(self, dirname, filename):
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        filepath = os.path.join(dirname, filename)
        self.image.save(filepath)
