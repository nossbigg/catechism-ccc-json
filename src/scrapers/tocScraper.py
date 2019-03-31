import requests
CATECHISM_URL = "http://www.vatican.va/archive/ENG0015/_INDEX.HTM"


def downloadTocHtml():
    return requests.get(CATECHISM_URL).text
