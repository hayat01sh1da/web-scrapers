from selenium.webdriver.common.by import By
from decimal_handler import *

def tag_elems_list(items, tag):
    elems_list = []
    for item in items:
        _elems_list = []
        for elem in item.find_elements(By.TAG_NAME, tag):
            _elems_list.append(elem.text)
        elems_list.append(_elems_list)
    return elems_list

def class_elems_list(items, klass):
    elems_list = []
    for item in items:
        _elems_list = []
        for elem in item.find_elements(By.CLASS_NAME , klass):
            if isfloat(elem.text):
                _elems_list.append(float(elem.text))
            else:
                _elems_list.append(elem.text)
        elems_list.append(_elems_list)
    return elems_list
