from src.scrapers.tocScraper import downloadTocHtml, saveTocToDisk

tocHtml = downloadTocHtml()
saveTocToDisk(tocHtml)