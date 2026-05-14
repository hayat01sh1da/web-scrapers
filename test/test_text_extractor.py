import csv
import os

from text_extractor import TextExtractor


_EXPECTED_LECTURER_INFO = [
    {'': '0', '項目': '講師名', '値': '今西 航平'},
    {'': '1', '項目': '所属企業', '値': '株式会社キカガク'},
    {'': '2', '項目': '生年月日', '値': '1994年7月15日'},
    {'': '3', '項目': '出身', '値': '千葉県'},
    {'': '4', '項目': '趣味', '値': 'バスケットボール、読書、ガジェット集め'},
]


def test_save_csv(tmp_dir):
    text_extractor = TextExtractor(init_webdriver=False)
    text_extractor.login('imanishi', 'kohei')
    filename = 'lecturer_info.csv'
    text_extractor.save_csv(tmp_dir, filename)
    filepath = os.path.join(tmp_dir, filename)
    with open(filepath) as f:
        lecturer_info = list(csv.DictReader(f))
    assert os.path.exists(filepath)
    assert lecturer_info == _EXPECTED_LECTURER_INFO
