from scrapers.tocScraper import downloadTocHtml, saveTocToDisk
from parsers.tocParser import parseToc
from scrapers.pageScraper import downloadPagesHtmls, savePagesToDisk
from scrapers.abbreviationsScraper import downloadAbbreviationsHtml, saveAbbreviationsToDisk

toc_html = downloadTocHtml()
saveTocToDisk(toc_html)

toc_link_tree, toc_nodes_dict = parseToc(toc_html)

pages_html_dict = downloadPagesHtmls(toc_nodes_dict)
savePagesToDisk(pages_html_dict)

abbreviations_html = downloadAbbreviationsHtml()
saveAbbreviationsToDisk(abbreviations_html)

print('Done!')
