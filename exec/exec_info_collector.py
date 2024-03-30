import os
import sys
sys.path.append('./src')
from info_collector import InfoCollector

info_collector = InfoCollector()
dirname        = os.path.join('.', 'csv')
filename       = 'tour_reviews.csv'

for i in range(1, 4):
    info_collector.save_csv(dirname, filename)
