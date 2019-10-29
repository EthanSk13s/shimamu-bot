import bs4 as bs

class Scraper():
    def __init__(self, url):
        self.url = url
        self.soup = bs.BeautifulSoup(url, 'lxml')

class CharaScraper(Scraper):   
    def summary(self):
        desc = self.soup.find('table', 
        {'class':'wikitable',
        'style': 'width:100%; text-align:center; text-size-adjust: none; margin-top:0;'}
        ) 

        return desc.text

    def title(self):
        title = self.soup.find('div', {'class': 'char-title'})
        tl1 = "This character's title is untranslated."
        tl2 = "This title is an unofficial, amateur translation."
        tl3 = "This title is a translation sourced from Granblue Fantasy"

        return title.text.strip(tl1).strip(tl2).strip(tl3)

    def name(self):
        name = self.soup.find('div', {'class': 'char-name'})

        return name.text

    def hp(self):
        hp = self.soup.find('td', {'style': 'width:65%;'})

        return hp.text

    def atk(self):
        table = self.soup.find('table', {'class': 'wikitable',
        'style': 'width: 100%; text-align:center; margin-top:2px; margin-left:auto; margin-right:auto;'})

        atk = table.find_all('td')

        return atk[1].text

    def image(self):
        imgs = self.soup.find('a', {'class': 'image'})
        img = imgs.find_all('img')

        return f"https://gbf.wiki{img[0]['src']}"

    def skills(self):
        table = self.soup.find_all('table', {'class': 'wikitable',
        'style': 'width:100%; text-align:center; text-size-adjust: none;'})

        raw_skills = table[1].find_all('td', {'class': 'skill-name'})
        skills = []

        for skill in raw_skills:
            skills.append(skill.text)

        return skills

    def element(self):
        table = self.soup.find('table', {'class': 'wikitable',
        'style': 'width: 100%; text-align:center; margin-top:2px; margin-left:auto; margin-right:auto;'})

        element = table.find('img')
        return f"https://gbf.wiki{element['src']}"