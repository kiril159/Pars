import requests
from bs4 import BeautifulSoup


def gas():
    url = 'https://student.itmo.ru/ru/scholarship_basic/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    info = []
    for i in soup.select('body > main > div > section > div > div.cell.lg-9.md-12.content-block > section > div'):
        title = i.select('div')
        for el in title[::4]:
            info.append(el.text)
    return info


def pgas():
    url = 'https://student.itmo.ru/ru/scholarship_up/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    info = []
    for i in soup.select(
            'body > main > div > section > div > div.cell.lg-9.md-12.content-block > section > div.accordion'):
        title = i.select('div')
        for el in title[::4]:
            info.append(el.text)
    return info


def mat_supp():
    url = 'https://student.itmo.ru/ru/scholarship_social_2/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    info = []
    for i in soup.select('body > main > div > section > div > div.cell.lg-9.md-12.content-block > section > div'):
        title = i.select('div')
        for el in title[::4]:
            info.append(el.text)
    return info


def soc_schol():
    url = 'https://student.itmo.ru/ru/scholarship_social/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    info = []
    for i in soup.select(
            'body > main > div > section > div > div.cell.lg-9.md-12.content-block > section > div.accordion'):
        title = i.select('div')
        for el in title[::4]:
            info.append(el.text)
    return info
