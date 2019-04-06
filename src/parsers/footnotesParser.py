from collections import namedtuple
PageFootnotes = namedtuple('PageFootnotes', 'mapping')
PageFootnote = namedtuple('PageFootnote', 'number text')


def extractStructuredFootnotes(raw_nodes):
    mapping = {}

    for index in range(0, len(raw_nodes), 2):
        footnote_number_node = raw_nodes[index].find('a')
        text_node = raw_nodes[index+1]

        footnote_number = int(footnote_number_node.text)
        text = text_node.text
        text = text.replace("⇒", "").strip()

        mapping[footnote_number] = PageFootnote(footnote_number, text)

    return PageFootnotes(mapping)
