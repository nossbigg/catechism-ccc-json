import requests
import os
from src.common.config import DATA_SAVE_PATH, CATECHISM_TOC_SAVE_PATH

CATECHISM_URL = "http://www.vatican.va/archive/ENG0015/_INDEX.HTM"


def downloadTocHtml():
    return requests.get(CATECHISM_URL).text


def saveTocToDisk(contents):
    os.makedirs(DATA_SAVE_PATH, exist_ok=True)
    with open(CATECHISM_TOC_SAVE_PATH, 'w+') as f:
        f.write(contents)
