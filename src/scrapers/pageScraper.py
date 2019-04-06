import requests


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
