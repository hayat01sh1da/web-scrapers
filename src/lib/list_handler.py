from typing import Any
from selenium.webdriver.common.by import By
from decimal_handler import DecimalHandler


class ListHandler:
    def __init__(self) -> None:
        self.decimal_handler = DecimalHandler()

    def tag_elems_list(self, items: Any, tag: str) -> list[list[str]]:
        elems_list = []
        for item in items:
            _elems_list = []
            for elem in item.find_elements(By.TAG_NAME, tag):
                _elems_list.append(elem.text)
            elems_list.append(_elems_list)
        return elems_list

    def class_elems_list(self, items: Any,
                         klass: str) -> list[list[Any]]:
        elems_list = []
        for item in items:
            _elems_list = []
            for elem in item.find_elements(By.CLASS_NAME, klass):
                if self.decimal_handler.is_float(elem.text):
                    _elems_list.append(float(elem.text))
                else:
                    _elems_list.append(elem.text)
            elems_list.append(_elems_list)
        return elems_list
