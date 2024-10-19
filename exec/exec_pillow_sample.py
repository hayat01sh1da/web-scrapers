import os
import sys
import shutil
import glob
sys.path.append('./src')
from pillow_sample import PillowSample

dirname  = os.path.join('.', 'imgs')
filename = 'bird{suffix}.jpg'
filepath = os.path.join(dirname, filename)

pillow_sample = PillowSample(filepath.format(suffix = ''))

pillow_sample.resize_image((1024, 768))
pillow_sample.save_image(dirname, filename.format(suffix = '_resized'))

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.isdir(pycache):
        shutil.rmtree(pycache)
