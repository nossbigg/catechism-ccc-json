from collections import namedtuple
import re

REFERENCE_ARROW_SYMBOL = '⇒'


PageFootnote = namedtuple('PageFootnote', 'number refs')
PageFootnoteRef = namedtuple('PageFootnoteRef', 'text link')


def extractStructuredFootnotes(raw_nodes):
    mapping = {}

    for index in range(0, len(raw_nodes), 2):
        footnote_number_node = raw_nodes[index].find('a')
        text_node = raw_nodes[index+1]

        footnote_number = int(footnote_number_node.text)
        refs = extractFootnoteRefs(text_node)

        mapping[footnote_number] = PageFootnote(footnote_number, refs)

    return mapping


def extractFootnoteRefs(footnote_node):
    footnote_text = footnote_node.text
    ref_texts = footnote_text.split(";")
    ref_texts = [cleanRefText(t) for t in ref_texts]

    reference_nodes = footnote_node.find_all('a')
    reference_links = get_links_from_anchors(reference_nodes)

    footnote_refs = []
    reference_links_iter = iter(reference_links)

    for text in ref_texts:
        if REFERENCE_ARROW_SYMBOL in text:
            footnote_refs.append(PageFootnoteRef(
                text, next(reference_links_iter)))
            continue

        footnote_refs.append(PageFootnoteRef(text, None))

    return footnote_refs


def cleanRefText(raw_text):
    t = raw_text
    t = t.replace('\n', " ")
    t = re.sub('[ ]+', " ", t)
    t = t.strip()
    return t


def get_links_from_anchors(anchor_nodes):
    return [node['href'] for node in anchor_nodes]
