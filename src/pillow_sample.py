from PIL import Image
import os
import sys
sys.path.append('./src')
from application import Application

class PillowSample(Application):
    def __init__(self, filepath):
        super().__init__()
        # Open the image using a context manager and copy it into memory so
        # the underlying file handle is closed promptly (prevents ResourceWarning).
        with Image.open(filepath) as img:
            self.image = img.copy()

    def resize_image(self, size):
        return self.image.resize(size).size

    def save_image(self, dirname, filename):
        os.makedirs(dirname, exist_ok = True)
        filepath = os.path.join(dirname, filename)
        self.image.save(filepath)
