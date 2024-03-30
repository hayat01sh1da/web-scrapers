import os
import sys
sys.path.append('./src')
from image_collector import ImageCollector

image_collector = ImageCollector()
dirname         = os.path.join('.', 'imgs')
filename        = 'image_{i:02}.jpg'

image_collector.save_images(dirname, filename)
