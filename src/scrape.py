from src.scrapers.tocScraper import downloadTocHtml, saveTocToDisk
from src.parsers.tocParser import parseToc
from src.scrapers.pageScraper import downloadPagesHtmls, savePagesToDisk
from src.parsers.pageParser import parsePages

toc_html = downloadTocHtml()
saveTocToDisk(toc_html)

toc_link_tree, toc_nodes_dict = parseToc(toc_html)

pages_html_dict = downloadPagesHtmls(toc_nodes_dict)
savePagesToDisk(pages_html_dict)

page_nodes_dict = parsePages(pages_html_dict)
