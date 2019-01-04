import Model.Domain as Domain
import Model.BlackList as BlackList
class Step1:
    def __init__ (self):
        self.response = 'False'
        self.blackList = BlackList.BlackList()
    
    def getResponse (self, domain:Domain.Domain):
        self.response = (domain.getDomainNameNetloc() in self.blackList.urlListModel.getUrlList())
        if(self.response):
            domain.setValutation(0,1)
        return self.response