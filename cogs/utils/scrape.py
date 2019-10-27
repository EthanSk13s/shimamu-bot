import bs4 as bs

def summary(url):

    soup = bs.BeautifulSoup(url, 'lxml')
    desc = soup.find('table', 
    {'class':'wikitable',
    'style': 'width:100%; text-align:center; text-size-adjust: none; margin-top:0;'}
    )
    pog = str(desc.find_all('td'))    
    thing = pog.strip('[').strip(']').strip('<td>').strip('</td>')

    return thing

