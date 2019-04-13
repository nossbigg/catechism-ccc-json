from src.scrapers.tocScraper import readTocFromDisk
from src.scrapers.pageScraper import readPagesFromDisk
from src.parsers.tocParser import parseToc
from src.parsers.pageParser import parsePages

toc_html = readTocFromDisk()
toc_link_tree, toc_nodes_dict = parseToc(toc_html)

pages_html_dict = readPagesFromDisk()
page_nodes_dict = parsePages(pages_html_dict)
