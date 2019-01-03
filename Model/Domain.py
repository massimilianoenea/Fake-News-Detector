from urllib.parse import urlparse
from collections import Counter
# from urlparse import urlparse  # Python 2
import Model.ExcludeList as Exclused
class Domain:

    def __init__(self, url):
        self.internalDomain = [url.lower()]
        self.baseUrl = url.lower()
        self.otherUrl = []
        self.exlusedUrl = Exclused.ExcludeList().urlListModel.getUrlList()

    def addDomain(self, url):
        if url.startswith("http"):
            self.internalDomain.append(url.lower())
            self.clearDomainArray()

    def addOtherDomain(self, url):
        exclude = False
        result = ""
        if url.startswith("http"):
            parsed_uri = urlparse(url.lower())
            result = '{uri.netloc}'.format(uri=parsed_uri)
            for exclused in self.exlusedUrl:
                if exclused.lower() in result.lower():
                    exclude = True
                    break
            if exclude is False:
                self.otherUrl.append(result)

    def getOccurrence(self):
        return Counter(self.otherUrl)
    
    def getOccurrenceInternal(self):
        return Counter(self.internalDomain)
    
    def getExcludedUrl(self):
        return self.exlusedUrl

    def internalUrl(self):
        return self.internalDomain

    def otherDomain(self):
        self.clearOtherDomainArray()
        return self.otherUrl

    def clearOtherDomainArray(self):
        self.otherUrl = list(set(self.otherUrl))

    def clearDomainArray(self):
        self.internalDomain = list(set(self.internalDomain))

    def getBaseUrl(self):
        return self.baseUrl

