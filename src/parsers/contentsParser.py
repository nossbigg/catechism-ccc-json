from collections import namedtuple
PageContents = namedtuple('PageContents', 'nodes')
PageContent = namedtuple('PageContent', 'text')


def extractStructuredContents(raw_nodes):
    return PageContents(raw_nodes)
