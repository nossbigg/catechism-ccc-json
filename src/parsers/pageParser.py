from collections import namedtuple
from bs4 import BeautifulSoup

PageContent = namedtuple('PageContent', 'id contents footnotes')


def parsePages(pages_html_dict):
    page_contents = [parsePage(e['html']) for e in pages_html_dict.values()]

    result = {}
    for toc_id, page_content in zip(pages_html_dict.keys(), page_contents):
        content_nodes, footnote_nodes = page_content
        result[toc_id] = PageContent(toc_id, content_nodes, footnote_nodes)
    return result


def parsePage(html_doc):
    soup = BeautifulSoup(html_doc, 'html5lib')

    content_start_node = getContentsFirstNode(soup)
    footnotes_start_node = getFootnotesFirstNode(soup)
    footer_node = getFooterFirstNode(soup)

    content_nodes = extractContentsNodes(
        content_start_node, footnotes_start_node, footer_node)
    footnote_nodes = extractFootnotesNodes(
        content_start_node, footnotes_start_node, footer_node)

    return content_nodes, footnote_nodes


def extractContentsNodes(content_start_node, footnotes_start_node, footer_node):
    result = []
    ending_node = footnotes_start_node if footnotes_start_node is not None else footer_node

    current_node = content_start_node.next_sibling
    while current_node is not ending_node:
        result.append(current_node)
        current_node = current_node.next_sibling
    return result


def extractFootnotesNodes(content_start_node, footnotes_start_node, footer_node):
    if footnotes_start_node is None:
        return []

    result = []
    current_node = footnotes_start_node.next_sibling
    while current_node is not footer_node:
        if current_node.name == 'font':
            result.append(current_node)
        current_node = current_node.next_sibling
    return result


def getContentsFirstNode(soup):
    hr_nodes = soup.select('body > hr')
    hr_content_start_node = hr_nodes[1]
    return hr_content_start_node


def getFooterFirstNode(soup):
    center_nodes = soup.select('body > center')
    footer_node = center_nodes[len(center_nodes) - 2]
    return footer_node


def getFootnotesFirstNode(soup):
    footnotes_nodes = soup.select('body > hr[width="30%"]')
    if len(footnotes_nodes) == 0:
        return None
    return footnotes_nodes[0]
