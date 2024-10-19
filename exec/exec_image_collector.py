import os
import sys
import shutil
import glob
sys.path.append('./src')
from image_collector import ImageCollector

image_collector = ImageCollector()
dirname         = os.path.join('.', 'imgs')
filename        = 'image_{i:02}.jpg'

image_collector.save_images(dirname, filename)

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.isdir(pycache):
        shutil.rmtree(pycache)
