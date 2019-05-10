import grequests
import os
import glob

from common.config import DATA_SAVE_PATH, PAGES_SAVE_PATH


def downloadPagesHtmls(toc_nodes_dict):
    result = {}

    toc_with_urls = [item for item in toc_nodes_dict.values()
                     if item.link is not None]

    requestItems = [grequests.get(e.link) for e in toc_with_urls]
    responses = grequests.map(requestItems)

    for response, toc_item in zip(responses, toc_with_urls):
        result[toc_item.id] = response.text

    return result


def savePagesToDisk(pages_html_dict):
    os.makedirs(PAGES_SAVE_PATH, exist_ok=True)

    for toc_id, html in pages_html_dict.items():
        file_save_path = os.path.join(PAGES_SAVE_PATH, toc_id + '.html')

        with open(file_save_path, 'w+') as f:
            f.write(html)


def readPagesFromDisk():
    result = {}

    page_html_files = glob.glob(PAGES_SAVE_PATH + "/*.html")
    page_html_files.sort()
    for file_path in page_html_files:
        with open(file_path, 'r') as f:
            toc_id = os.path.basename(f.name).split('.')[0]
            contents = f.read()
            result[toc_id] = contents

    return result
