import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

class TextExtractor:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        self.chrome = webdriver.Chrome(service=Service(os.environ['PATH_TO_WEBDRIVER']), options=options)
        self.chrome.get(url)

    def login(self, user_name, pwd):
        username = self.chrome.find_element(By.ID, 'username')
        username.send_keys(user_name)
        password = self.chrome.find_element(By.ID, 'password')
        password.send_keys(pwd)
        login = self.chrome.find_element(By.ID, 'login-btn')
        login.click()

    def get_lecturer_info(self):
        ths = self.chrome.find_elements(By.TAG_NAME, 'th')
        keys = []
        for th in ths:
            keys.append(th.text)
        tds = self.chrome.find_elements(By.TAG_NAME, 'td')
        vals = []
        for td in tds:
            if '\n' in td.text:
                vals.append(td.text.replace('\n', '、'))
            else:
                vals.append(td.text)
        profile = {}
        for i in range(len(keys)):
            profile[keys[i]] = vals[i]
        return profile, keys, vals

    def export_csv(self, keys, vals, path):
        df = pd.DataFrame()
        df['項目'] = keys
        df['値'] = vals
        df.to_csv(path)
