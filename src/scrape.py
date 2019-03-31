from src.scrapers.tocScraper import downloadTocHtml, saveTocToDisk
from src.parsers.tocParser import parseToc

tocHtml = downloadTocHtml()
saveTocToDisk(tocHtml)

tocLinks = parseToc(tocHtml)
