import bs4 as bs

class Scraper():
    def __init__(self, url):
        self.url = url
        self.soup = bs.BeautifulSoup(url, 'lxml')

class CharaScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)
    
    def summary(self):

        desc = self.soup.find('table', 
        {'class':'wikitable',
        'style': 'width:100%; text-align:center; text-size-adjust: none; margin-top:0;'}
        )
        pog = str(desc.find_all('td'))    
        thing = pog.strip('[').strip(']').strip('<td>').strip('</td>')

        return thing

