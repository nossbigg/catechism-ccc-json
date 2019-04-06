from src.scrapers.tocScraper import downloadTocHtml, saveTocToDisk
from src.parsers.tocParser import parseToc
from src.scrapers.pageScraper import downloadPagesHtmls

toc_html = downloadTocHtml()
saveTocToDisk(toc_html)

toc_link_tree, toc_nodes_dict = parseToc(toc_html)

pages_html = downloadPagesHtmls(toc_nodes_dict)
