from bs4 import BeautifulSoup
from collections import namedtuple

Abbreviation = namedtuple('Abbreviation', 'shorthand text')


def parseAbbreviations(abbreviations_html):
    bible_refs = {}
    other_refs = {}

    soup = BeautifulSoup(abbreviations_html, 'html5lib')
    addToBibleRefs = False

    for tr_node in soup.select('tbody > tr'):
        if containsBibleTd(tr_node):
            addToBibleRefs = True
            continue

        td_nodes = tr_node.select('td')
        abbr_shorthand = td_nodes[0].text
        abbr_full = td_nodes[1].text
        abbr = Abbreviation(abbr_shorthand, abbr_full)

        if addToBibleRefs:
            bible_refs[abbr_shorthand] = abbr
        else:
            other_refs[abbr_shorthand] = abbr

    return bible_refs, other_refs


def containsBibleTd(tr_node):
    return len(tr_node.select('td[colspan="2"]')) > 0
