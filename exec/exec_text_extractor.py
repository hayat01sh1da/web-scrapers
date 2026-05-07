from text_extractor import TextExtractor
import os
import sys
import shutil
import glob
sys.path.append('./src')

text_extractor = TextExtractor()
text_extractor.login('imanishi', 'kohei')
dirname = os.path.join('.', 'csv')
filename = 'lecturer_info.csv'

text_extractor.save_csv(dirname, filename)

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive=True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
