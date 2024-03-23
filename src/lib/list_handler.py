from selenium.webdriver.common.by import By
from decimal_handler import DecimalHandler

class ListHandler:
    def __init__(self):
        self.decimal_handler = DecimalHandler()

    def tag_elems_list(self, items, tag):
        elems_list = []
        for item in items:
            _elems_list = []
            for elem in item.find_elements(By.TAG_NAME, tag):
                _elems_list.append(elem.text)
            elems_list.append(_elems_list)
        return elems_list

    def class_elems_list(self, items, klass):
        elems_list = []
        for item in items:
            _elems_list = []
            for elem in item.find_elements(By.CLASS_NAME , klass):
                if self.decimal_handler.is_float(elem.text):
                    _elems_list.append(float(elem.text))
                else:
                    _elems_list.append(elem.text)
            elems_list.append(_elems_list)
        return elems_list
