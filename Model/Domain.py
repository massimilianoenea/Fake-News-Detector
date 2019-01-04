from urllib.parse import urlparse
from collections import Counter
# from urlparse import urlparse  # Python 2
import Model.ExcludeList as Exclused
class Domain:

    def __init__(self, url):
        parsed_uri = urlparse(url.lower())
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        self.baseUrl = result
        self.internalDomain = [self.baseUrl]
        result = '{uri.netloc}'.format(uri=parsed_uri)
        self.domainNameNetloc = result
        self.otherUrl = []
        self.exlusedUrl = Exclused.ExcludeList().urlListModel.getUrlList()
        self.brand = ""
        self.description = ""
        self.categories = []
        self.valutation = [0,0,0,0,0,0]    

    def setDescription (self, description):
        self.description = description

    def setCategory (self, category):
        self.categories.append(category)

    def setCategoryArray (self, array):
        self.categories = array  

    def setBrand (self, brand):
        self.brand = brand

    def addDomain(self, url):
        if url.startswith("http"):
            self.internalDomain.append(url.lower())
            self.clearDomainArray()

    def setInternalDomainArray(self,array):
        self.internalDomain = array
    
    def setInternalDomain(self,url):
        self.internalDomain.append(url)
    
    def setOtherDomainArray(self,array):
        self.otherUrl= []
        for url in array:
            if url not in self.exlusedUrl:
                self.otherUrl.append(url)

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

    def getDomainNameNetloc(self):
        return self.domainNameNetloc

    def setValutation(self, position, value):
        self.valutation[position] = value
