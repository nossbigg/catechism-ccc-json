import requests
from src.common.config import ABBREVIATIONS_SAVE_PATH

ABBREVIATIONS_URL = 'http://www.scborromeo.org/mobileccc/abbrev.htm'


def downloadAbbreviationsHtml():
    return requests.get(ABBREVIATIONS_URL).text


def saveAbbreviationsToDisk(contents):
    with open(ABBREVIATIONS_SAVE_PATH, 'w+') as f:
        f.write(contents)


def readAbbreviationsFromDisk():
    with open(ABBREVIATIONS_SAVE_PATH, 'r') as f:
        contents = f.read()
    return contents
