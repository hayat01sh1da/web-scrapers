from selenium.webdriver.common.by import By
import pandas as pd
import os
import sys
sys.path.append('./src')
from application import Application

class TextExtractor(Application):
    def __init__(self):
        super().__init__()
        self.url = '{base_url}/{path}'.format(base_url = self.base_url, path = 'login_page')

    def login(self, user_name, pwd):
        self.chrome.get(self.url)
        username = self.chrome.find_element(By.ID, 'username')
        password = self.chrome.find_element(By.ID, 'password')
        login    = self.chrome.find_element(By.ID, 'login-btn')
        username.send_keys(user_name)
        password.send_keys(pwd)
        login.click()

    def get_lecturer_info(self):
        ths  = self.chrome.find_elements(By.TAG_NAME, 'th')
        keys = []
        for th in ths:
            keys.append(th.text)
        tds  = self.chrome.find_elements(By.TAG_NAME, 'td')
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

    def export_csv(self, keys, vals, dirname, filename):
        df         = pd.DataFrame()
        df['項目'] = keys
        df['値']   = vals

        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        filepath = os.path.join(dirname, filename)
        df.to_csv(filepath)
