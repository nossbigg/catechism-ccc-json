from scrapers.tocScraper import readTocFromDisk
from scrapers.pageScraper import readPagesFromDisk
from scrapers.abbreviationsScraper import readAbbreviationsFromDisk
from parsers.tocParser import parseToc
from parsers.pageParser import parsePages
from parsers.abbreviationsParser import parseAbbreviations
from exporters.jsonExporter import exportStoreAsJson

toc_html = readTocFromDisk()
toc_link_tree, toc_nodes_dict = parseToc(toc_html)

abbreviations_html = readAbbreviationsFromDisk()
bible_refs, other_refs = parseAbbreviations(abbreviations_html)

pages_html_dict = readPagesFromDisk()
page_nodes_dict = parsePages(pages_html_dict)

exportStoreAsJson(toc_link_tree, toc_nodes_dict,
                  page_nodes_dict, bible_refs, other_refs)
