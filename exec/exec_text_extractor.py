import os
import sys
sys.path.append('./src')
from text_extractor import TextExtractor

text_extractor = TextExtractor()
text_extractor.login('imanishi', 'kohei')
dirname  = os.path.join('.', 'csv')
filename = 'lecturer_info.csv'

text_extractor.save_csv(dirname, filename)
