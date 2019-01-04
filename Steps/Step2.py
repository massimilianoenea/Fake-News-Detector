import Model.Domain as Domain
import Model.BlackList as BlackList
import Model.ExcludeList as ExcludeList
from urllib.parse import urlparse

import requests
import newspaper
from bs4 import BeautifulSoup
class Step2:
    def __init__ (self):
        self.domainList = []
        self.excludeList = ExcludeList.ExcludeList().urlListModel.getUrlList()
        self.blackList = BlackList.BlackList().urlListModel.getUrlList()
    
    def checkRefToOtherSite (self, domain:Domain.Domain):
        
        #toFetchSite = newspaper.build(domain.getBaseUrl(), language='it')
        #for article in toFetchSite.articles:
            #domain.setInternalDomain(article.url)
        #domain.setDescription = toFetchSite.description
        #domain.setCategoryArray = toFetchSite.category_urls

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
        
        counter = 0

        for url in domain.otherDomain():
            parsed_uri = urlparse(url)
            url = '{uri.netloc}'.format(uri=parsed_uri)
            for black in self.blackList:
                if black.lower().find(url.lower()):
                    counter += 1
            #if url in self.blackList:
            #    counter += 1

        domain.setValutation(1,(counter/len(domain.otherDomain())))

        return domain.otherDomain()