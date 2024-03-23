import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import sys
sys.path.append('./src/lib')
from list_handler import *

class InfoCollector:
    def __init__(self, base_url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        self.chrome = webdriver.Chrome(service=Service(os.environ['PATH_TO_WEBDRIVER']), options=options)
        self.base_url = base_url

    def _get_url(self, query_str=''):
        url = self.base_url + query_str
        self.chrome.get(url)

    def _get_ranking_items(self):
        elem_ranking_items = self.chrome.find_elements(By.CLASS_NAME, 'u_categoryTipsItem')
        return elem_ranking_items

    def get_titles(self, query_str):
        self._get_url(query_str)
        elem_titles = self.chrome.find_elements(By.CLASS_NAME, 'u_title')
        titles = []
        for elem_title in elem_titles:
            titles.append(elem_title.text.split('\n')[-1])
        return titles

    def get_evaluations(self, query_str):
        self._get_url(query_str)
        elem_rank_boxes = self.chrome.find_elements(By.CLASS_NAME, 'u_rankBox')
        evaluations = []
        for elem_rank_box in elem_rank_boxes:
            evaluations.append(float(elem_rank_box.find_element(By.CLASS_NAME, 'evaluateNumber').text))
        return evaluations

    def get_categories(self):
        self._get_url()
        elem_ranking_items = self._get_ranking_items()
        categories = tag_elems_list(elem_ranking_items, 'dt')
        return categories[0]

    def get_rankings(self, query_str):
        self._get_url(query_str)
        elem_ranking_items = self._get_ranking_items()
        rankings = class_elems_list(elem_ranking_items, 'is_rank')
        return rankings

    def get_comments(self, query_str):
        self._get_url(query_str)
        elem_ranking_items = self._get_ranking_items()
        comments = class_elems_list(elem_ranking_items, 'comment')
        return comments

    def export_csv(self, titles, evaluations, rankings, categories, path):
        df = pd.DataFrame()
        df['観光地'] = titles
        df['総合評価'] = evaluations
        df_rankings = pd.DataFrame(rankings)
        df_rankings.columns = categories
        df = pd.concat([df, df_rankings], axis=1)
        df.to_csv(path)
