import Model.Domain as Domain
import Model.BlackList as BlackList
import Model.ExcludeList as ExcludeList
import requests
from bs4 import BeautifulSoup
class Step2:
    def __init__ (self):
        self.domainList = []
        self.excludeList = ExcludeList.ExcludeList().urlListModel.getUrlList()
        self.blackList = BlackList.BlackList().urlListModel.getUrlList()
    
    def checkRefToOtherSite (self, domain:Domain.Domain):
        for url in domain.internalUrl():
            r = requests.get(url)
            html = BeautifulSoup(r.content, 'html.parser')
            for a in html.find_all('a', href=True):
                href = a['href']
                if href.startswith(domain.baseUrl):
                    domain.addDomain(href)

        for url in domain.internalUrl():
            r = requests.get(url)
            html = BeautifulSoup(r.content, 'html.parser')
            for a in html.find_all('a', href=True):
                href = a['href']
                if not href.startswith(domain.baseUrl):
                    domain.addOtherDomain(href)            

        return domain.otherDomain()