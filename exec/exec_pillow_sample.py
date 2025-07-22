import os
import sys
import shutil
import glob
sys.path.append('./src')
from pillow_sample import PillowSample

dirname           = os.path.join('.', 'imgs')
original_filename = 'bird.jpg'
resized_filename  = 'bird_resized.jpg'
original_filepath = os.path.join(dirname, original_filename)

pillow_sample = PillowSample(original_filepath)

pillow_sample.resize_image((1024, 768))
pillow_sample.save_image(dirname, resized_filename)

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
