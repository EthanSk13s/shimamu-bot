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
        headers = {
            'tl1': "This character's title is untranslated.",
            'tl2': "This title is an unofficial, amateur translation.",
            'tl3': "This title is a translation sourced from Granblue Fantasy"
        }
        for header in headers.values():
            if header in title.text:
                new_title = title.text.strip(header)
                break

        return new_title

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

class RaidScraper(Scraper):
    def __init__(self, url, difficulty: str):
        super().__init__(url)

        self.diff = difficulty.capitalize()
        self.tables = self.soup.find('div', {'class': 'tabbertab',
        'title': self.diff})

    def name(self):
        raid_name = self.tables.find('div', {'style': 'position: relative'})

        return raid_name.text.replace('Edit battle', '')

    def cost(self):
        cost = self.tables.find('td', {'style': 'width: 33%'})

        return cost.text.replace("Cost to Host:", '') 

    def unlock(self):
        table = self.tables.find('table', {'class': 'wikitable',
        'style': 'width: 100%; margin-bottom: 0;'})

        unlock = table.find_all('td', {'style': 'width: 33%'})

        return unlock[2].text.replace('Unlock:', '')

    def location(self):
        table = self.tables.find('table', {'class': 'wikitable',
        'style': 'width: 100%; margin-bottom: 0;'})

        location = table.find_all('td', {'colspan': True})

        return location[0].text.replace('Location:', '')

    def image(self):
        image = self.tables.find('img', {'width': '180', 'height': '126'})

        return f"https://gbf.wiki{image['src']}"


