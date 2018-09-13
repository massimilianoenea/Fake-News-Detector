import requests
import Model.Domain as urlDomain
import Model.UrlMatrix as urlMatrix
from progress.bar import Bar
from bs4 import BeautifulSoup

"""
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
"""

file = open('./domainList.txt', 'r')
fileExclude = open('./excludeList.txt', 'r')

domainList = []
excludeList = []

for line in fileExclude.read().splitlines():
    excludeList.append(line)

for line in file.read().splitlines():
    domainList.append(urlDomain.Domain(line, excludeList))

for domain in domainList:
    print(domain.domain())
    for url in domain.domain():
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        for a in html.find_all('a', href=True):
            href = a['href']
            if href.startswith(domain.baseUrl):
                domain.addDomain(href)

    print(len(domain.domain()), "own per il dominio ", domain.baseUrl)

    bar = Bar('Processin:', max=len(domain.domain()))

    for url in domain.domain():
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')
        for a in html.find_all('a', href=True):
            href = a['href']
            if not href.startswith(domain.baseUrl):
                domain.addOtherDomain(href)
        bar.next()
    bar.finish()

    print(len(domain.otherDomain()), "other per il dominio ", domain.baseUrl)

"""
    for url in domain.getOccurrence():
        print(url, " -> ", domain.getOccurrence()[url])
"""
