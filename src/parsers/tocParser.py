
from collections import namedtuple
from bs4 import BeautifulSoup
from src.common.NodeIdGenerator import NodeIdGenerator
CATECHISM_BASE_URL = 'http://www.vatican.va/archive/ENG0015/'


TocRawLink = namedtuple('TocRawLink', 'id indent_level text link')
TocLink = namedtuple('TocLink', 'id children')


def parseToc(html_doc):
    id_generator = NodeIdGenerator('toc')
    soup = BeautifulSoup(html_doc, 'html5lib')

    toc_root = soup.select("body > font")[0]
    toc_raw_links = parseNode(toc_root.find(
        "ul", recursive=False), 0, id_generator)

    toc_link_tree = createTocLinkTree(toc_raw_links, 1)
    toc_nodes_dict = createTocNodesDict(toc_raw_links)
    return toc_link_tree, toc_nodes_dict


def parseNode(ul_node_tag, indent_level, id_generator):
    if ul_node_tag is None:
        return []

    nodes = []

    for node in ul_node_tag.children:
        if node.name is None:
            continue

        new_indent_level = indent_level + 1 if node.name == "li" else indent_level
        if node.name == "font":
            nodes.append(
                createTocRawLink(id_generator.generate_id(),
                                 node,
                                 new_indent_level
                                 ))

        nodes = nodes + parseNode(node, new_indent_level, id_generator)

    return nodes


def createTocLinkTree(raw_links, indent_level):
    blocks = []
    present_block = []
    for link in raw_links:
        if link.indent_level == indent_level and len(present_block) > 0:
            blocks.append(present_block)
            present_block = []

        present_block.append(link)

    if len(present_block) > 0:
        blocks.append(present_block)

    links = []
    for block in blocks:
        head_node = block[0]
        children = createTocLinkTree(block[1:], indent_level + 1)
        links.append(TocLink(head_node.id, children))

    return links


def createTocRawLink(toc_id, font_node, indent_level):
    link = None
    link_node = font_node.find('a')
    if(link_node):
        link = CATECHISM_BASE_URL + link_node['href']

    return TocRawLink(toc_id, indent_level, font_node.text, link)


def createTocNodesDict(raw_links):
    toc_nodes_dict = {}
    for link in raw_links:
        toc_nodes_dict[link.id] = link

    return toc_nodes_dict
