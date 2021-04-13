import requests
from bs4 import BeautifulSoup as bs

class PageFormatter:

    def __init__(self, pg_soup):
        self.pg_soup = pg_soup
        self.min_length = 150

    def del_br(self):
        for e in self.pg_soup.findAll('br'):
            e.extract()

    def get_sections(self):
        sections = []
        for btag in self.pg_soup.find_all('b')[4:]:
            text_content = btag.next_sibling
            if text_content:
                if len(text_content) > self.min_length:
                    sections.append(text_content)
        return sections

if __name__ == "__main__":
    mainurl = "https://www.mtsamples.com"
    result = requests.get(mainurl+"/site/pages/sitemap.asp")

    print("Status:", result.status_code)

    src = result.content
    soup = bs(src, 'lxml')
    transcriptions = []

    urls = soup.find_all("a")
    asplinks = urls[139:-11]
    hreflinks = [asp['href'] for asp in asplinks if asp['href'].startswith('/site')]
    
    for idx,hrefs in enumerate(hreflinks):
        print("Scraping page ... ", idx)
        page = requests.get(mainurl+hrefs)
        pg_soup = bs(page.content, 'lxml')
        pf = PageFormatter(pg_soup)
        pf.del_br()
        transcript = pf.get_sections()
        transcriptions.extend(transcript)

    with open("mtsamples.txt", 'w') as f:
        for transcript in transcriptions:
            f.write("%s\n" %transcript)
