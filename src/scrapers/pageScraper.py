import grequests
import os

from src.common.config import DATA_SAVE_PATH, PAGES_SAVE_PATH


def downloadPagesHtmls(toc_nodes_dict):
    result = {}

    toc_with_urls = [item for item in toc_nodes_dict.values()
                     if item.link is not None]

    requestItems = [grequests.get(e.link) for e in toc_with_urls]
    responses = grequests.map(requestItems)

    for response, toc_item in zip(responses, toc_with_urls):
        result[toc_item.id] = {
            'node': toc_item,
            'html': response.text
        }

    return result


def savePagesToDisk(pages_html_dict):
    os.makedirs(PAGES_SAVE_PATH, exist_ok=True)

    for toc_id, item in pages_html_dict.items():
        file_save_path = os.path.join(PAGES_SAVE_PATH, toc_id + '.html')

        with open(file_save_path, 'w+') as f:
            f.write(item['html'])
