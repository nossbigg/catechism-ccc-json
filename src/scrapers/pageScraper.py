import requests
import os

from src.common.config import DATA_SAVE_PATH, PAGES_SAVE_PATH


def downloadPagesHtmls(toc_nodes_dict):
    result = {}

    for toc_id, toc_item in toc_nodes_dict.items():
        page_url = toc_item.link
        if page_url is None:
            continue

        result[toc_id] = {
            'node': toc_item,
            'html': requests.get(page_url).text
        }

    return result


def savePagesToDisk(pages_html_dict):
    os.makedirs(PAGES_SAVE_PATH, exist_ok=True)

    for toc_id, item in pages_html_dict.items():
        file_save_path = os.path.join(PAGES_SAVE_PATH, toc_id + '.html')

        with open(file_save_path, 'w+') as f:
            f.write(item['html'])
