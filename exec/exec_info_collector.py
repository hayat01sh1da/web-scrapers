import os
import sys
import shutil
import glob
sys.path.append('./src')
from info_collector import InfoCollector

info_collector = InfoCollector()
dirname        = os.path.join('.', 'csv')
filename       = 'tour_reviews.csv'

for i in range(1, 4):
    info_collector.save_csv(dirname, filename)

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.isdir(pycache):
        shutil.rmtree(pycache)
