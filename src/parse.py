from scrapers.tocScraper import readTocFromDisk
from scrapers.pageScraper import readPagesFromDisk
from scrapers.abbreviationsScraper import readAbbreviationsFromDisk

from parsers.tocParser import parseToc
from parsers.pageParser import parsePages
from parsers.specificPagesFixer import fixSpecificPagesHtml
from parsers.abbreviationsParser import parseAbbreviations

from exporters.jsonExporter import exportStoreAsJson
from exporters.jsonMetaGenerator import generate_store_meta

toc_html = readTocFromDisk()
toc_link_tree, toc_nodes_dict = parseToc(toc_html)

abbreviations_html = readAbbreviationsFromDisk()
bible_refs, other_refs = parseAbbreviations(abbreviations_html)
ccc_refs = {'bible': bible_refs, 'other': other_refs}

pages_html_dict = fixSpecificPagesHtml(readPagesFromDisk())
page_nodes_dict = parsePages(pages_html_dict)

meta = generate_store_meta()

exportStoreAsJson(toc_link_tree, toc_nodes_dict,
                  page_nodes_dict, ccc_refs, meta)
