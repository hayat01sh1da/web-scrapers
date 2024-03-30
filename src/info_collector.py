from selenium.webdriver.common.by import By
import pandas as pd
import os
import sys
sys.path.append('./src')
sys.path.append('./src/lib')
from list_handler import ListHandler
from application import Application

class InfoCollector(Application):
    def __init__(self):
        super().__init__()
        self.url          = '{base_url}/{path}'.format(base_url = self.base_url, path = 'ranking')
        self.list_handler = ListHandler()

    def save_csv(self, dirname, filename):
        _titles      = []
        _evaluations = []
        _rankings    = []

        for i in range(1, 4):
            _titles.append(self.__get_titles__(i))
            _evaluations.append(self.__get_evaluations__(i))
            _rankings.append(self.__get_rankings__(i))

        titles      = sum(_titles, [])
        evaluations = sum(_evaluations, [])
        rankings    = sum(_rankings, [])

        df                  = pd.DataFrame()
        df['観光地']         = titles
        df['総合評価']       = evaluations
        df_rankings         = pd.DataFrame(rankings)
        df_rankings.columns = self.__get_categories__()
        df                  = pd.concat([df, df_rankings], axis = 1)

        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        filepath = os.path.join(dirname, filename)
        df.to_csv(filepath)

    # private

    def __get_url__(self, i = None):
        if i == None:
            target_url = self.url
        else:
            target_url = '{url}?page={i}'.format(url = self.url, i = i)
        self.chrome.get(target_url)

    def __get_titles__(self, i):
        self.__get_url__(i)
        elem_titles = self.chrome.find_elements(By.CLASS_NAME, 'u_title')
        titles      = []
        for elem_title in elem_titles:
            titles.append(elem_title.text.split('\n')[-1])
        return titles

    def __get_evaluations__(self, i):
        self.__get_url__(i)
        elem_rank_boxes = self.chrome.find_elements(By.CLASS_NAME, 'u_rankBox')
        evaluations     = []
        for elem_rank_box in elem_rank_boxes:
            evaluations.append(float(elem_rank_box.find_element(By.CLASS_NAME, 'evaluateNumber').text))
        return evaluations

    def __get_ranking_items__(self):
        elem_ranking_items = self.chrome.find_elements(By.CLASS_NAME, 'u_categoryTipsItem')
        return elem_ranking_items

    def __get_rankings__(self, i):
        self.__get_url__(i)
        elem_ranking_items = self.__get_ranking_items__()
        rankings           = self.list_handler.class_elems_list(elem_ranking_items, 'is_rank')
        return rankings

    def __get_categories__(self):
        self.__get_url__()
        elem_ranking_items = self.__get_ranking_items__()
        categories         = self.list_handler.tag_elems_list(elem_ranking_items, 'dt')
        return categories[0]

    def __get_comments__(self, query_string):
        self.__get_url__(query_string)
        elem_ranking_items = self.__get_ranking_items__()
        comments           = self.list_handler.class_elems_list(elem_ranking_items, 'comment')
        return comments
