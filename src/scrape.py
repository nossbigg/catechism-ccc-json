from src.scrapers.tocScraper import downloadTocHtml, saveTocToDisk
from src.parsers.tocParser import parseToc
from src.scrapers.pageScraper import downloadPagesHtmls, savePagesToDisk

toc_html = downloadTocHtml()
saveTocToDisk(toc_html)

toc_link_tree, toc_nodes_dict = parseToc(toc_html)

pages_html_dict = downloadPagesHtmls(toc_nodes_dict)
savePagesToDisk(pages_html_dict)
