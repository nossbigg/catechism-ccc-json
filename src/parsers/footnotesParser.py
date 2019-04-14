from collections import namedtuple
import re

PageFootnotes = namedtuple('PageFootnotes', 'mapping')
PageFootnote = namedtuple('PageFootnote', 'number refs')
PageFootnoteRef = namedtuple('PageFootnoteRef', 'text')


def extractStructuredFootnotes(raw_nodes):
    mapping = {}

    for index in range(0, len(raw_nodes), 2):
        footnote_number_node = raw_nodes[index].find('a')
        text_node = raw_nodes[index+1]

        footnote_number = int(footnote_number_node.text)
        refs = extractFootnoteRefs(text_node.text)

        mapping[footnote_number] = PageFootnote(footnote_number, refs)

    return PageFootnotes(mapping)


def extractFootnoteRefs(footnote_text):
    ref_texts = footnote_text.split(";")
    ref_texts = [cleanRefText(t) for t in ref_texts]
    return [PageFootnoteRef(text) for text in ref_texts]


def cleanRefText(raw_text):
    t = raw_text
    t = t.replace('\n', " ")
    t = t.replace('\xa0', " ")
    t = re.sub('[ ]+', " ", t)
    t = t.strip()
    return t
