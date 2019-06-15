import re
from collections import namedtuple
PageContent = namedtuple('PageContent', 'text')
Paragraph = namedtuple('Paragraph', 'elements attrs')

cccReferenceLineMatcher = re.compile('(^[0-9]+) (.*)')


def extractStructuredContents(raw_nodes):
    paragraphs = []
    for n in raw_nodes:
        paragraphs = paragraphs + processElement(n)

    paragraphs = [transformCCCReferenceLine(p) for p in paragraphs]
    return paragraphs


def processElement(node):
    if node.name == 'br':
        return [createEmptyParagraph()]

    if node.name != 'p':
        return []

    flattened_text = node.text.replace('\n', ' ')
    if isEmptyOutput(flattened_text):
        return []

    children = []
    for paragraph_node in node.children:
        children = children + processParagraphChild(paragraph_node, {})

    return [createParagraph(node, children)]


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
        if isEmptyOutput(node.string):
            return []

        return [processTextElement(node, attrs)]

    return []


def transformCCCReferenceLine(paragraph):
    if not hasCCCReferenceLine(paragraph):
        return paragraph

    elements = paragraph.elements
    first_element = elements[0]
    rest_elements = elements[1:]

    ccc_ref_element, new_text_element = splitCCCReferenceFromTextElement(
        first_element)

    new_elements = [ccc_ref_element, new_text_element] + rest_elements
    new_paragrah = Paragraph(new_elements, paragraph.attrs)
    return new_paragrah


def hasCCCReferenceLine(paragraph):
    first_element = paragraph.elements[0]
    if 'text' not in first_element:
        return False

    return cccReferenceLineMatcher.match(first_element['text'])


def splitCCCReferenceFromTextElement(element):
    text_match = cccReferenceLineMatcher.match(element['text'])
    element_attrs = element['attrs']

    ccc_ref_element = createCCCRefElement(
        int(text_match.group(1)), element_attrs)
    new_text_element = createTextElement(text_match.group(2), element_attrs)

    return ccc_ref_element, new_text_element


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
    return {'type': 'ref', 'number': ref_number}


def processAnchorElement(node, attrs):
    return {'type': 'ref-anchor', 'link': node.get('href'), 'attrs': attrs}


def createSpacerElement():
    return {'type': 'spacer'}


def createTextElement(text, attrs):
    return {'type': 'text', 'text': text, 'attrs': attrs}


def createCCCRefElement(ref_number, attrs):
    return {'type': 'ref-ccc', 'ref_number': ref_number}


def createParagraph(node, children):
    attrs = {}
    if isIndentedParagraph(node):
        attrs['indent'] = True

    return Paragraph(children, attrs)

def createEmptyParagraph():
    return Paragraph([createSpacerElement()], {})


def isIndentedParagraph(node):
    style = node.get('style')
    if style is None:
        return False

    return 'margin-left:35.4pt' in style


def isEmptyOutput(node_text):
    text = node_text.replace('\n', "").strip()
    return len(text) == 0
