import re
from collections import namedtuple
PageContents = namedtuple('PageContents', 'nodes')
PageContent = namedtuple('PageContent', 'text')
Paragraph = namedtuple('Paragraph', 'children')

cccReferencedLineMatcher = re.compile('^[0-9]+ ')


def extractStructuredContents(raw_nodes):
    result = []
    for n in raw_nodes:
        result = result + processElement(n)

    return PageContents(result)


def processElement(node):
    if node.name == 'br':
        return [createSpacerElement()]

    if node.name != 'p':
        return []

    flattened_text = node.text.replace('\n', ' ')
    if isEmptyOutput(flattened_text):
        return []

    children = []
    for paragraph_node in node.children:
        children = children + processParagraphChild(paragraph_node, {})

    return [Paragraph(children)]


def processParagraphChild(node, attrs):
    if node is None:
        return []

    new_attrs = attrs
    if node.name == 'i':
        new_attrs['i'] = True
        return unwrapChildren(node, new_attrs)

    if node.name == 'b':
        new_attrs['b'] = True
        if node.get('style') is not None:
            new_attrs['heavy_header'] = True
        return unwrapChildren(node, new_attrs)

    if node.name == 'br':
        return [createSpacerElement()]

    if node.name == 'font':
        return [processFontElement(node, attrs)]

    if node.name == 'a':
        return [processAnchorElement(node, attrs)]

    if node.name == None:
        return [processTextElement(node, attrs)]

    return []


def unwrapChildren(node, attrs):
    result = []
    for n in node.children:
        result = result + processParagraphChild(n, attrs)

    return result


def processTextElement(node, attrs):
    text = node.string.replace('\n', ' ')
    return {'type': 'text', 'text': text, 'attrs': attrs}


def processFontElement(node, attrs):
    ref_number = int(node.text)
    return {'type': 'ref', 'number': ref_number, 'attrs': attrs}


def processAnchorElement(node, attrs):
    return {'type': 'ref', 'link': node.get('href'), 'attrs': attrs}


def createSpacerElement():
    return {'type': 'spacer'}


def isEmptyOutput(node_text):
    text = node_text.replace('\n', "").strip()
    return len(text) == 0


def isCCCReferenceLine(node_text):
    return cccReferencedLineMatcher.match(node_text)
