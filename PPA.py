import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://student.itmo.ru/ru/repeat_interim_exams/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    info = []
    for i in soup.select("body > main > div > section > div > div.cell.lg-9.md-12.content-block > section > section"):
        title = i.select('p')
        for el in title:
            info.append(el.text)
    return info
