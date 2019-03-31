
from collections import namedtuple
from bs4 import BeautifulSoup
CATECHISM_BASE_URL = 'http://www.vatican.va/archive/ENG0015/'


TocLink = namedtuple('TocLink', 'indent_level text link')


def parseToc(html_doc):
    soup = BeautifulSoup(html_doc, 'html5lib')

    toc_root = soup.select("body > font")[0]
    toc_links = parseNode(toc_root.find("ul", recursive=False), 0)
    return toc_links


def parseNode(ul_node_tag, indent_level):
    if ul_node_tag is None:
        return []

    nodes = []

    for node in ul_node_tag.children:
        if node.name is None:
            continue

        new_indent_level = indent_level + 1 if node.name == "li" else indent_level
        if node.name == "font":
            nodes.append(createTocLink(node, new_indent_level))

        nodes = nodes + parseNode(node, new_indent_level)

    return nodes


def createTocLink(font_node, indent_level):
    link = None
    link_node = font_node.find('a')
    if(link_node):
        link = CATECHISM_BASE_URL + link_node['href']

    return TocLink(indent_level, font_node.text, link)
