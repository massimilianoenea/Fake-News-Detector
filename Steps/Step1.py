import Model.Domain as Domain
import Model.BlackList as BlackList
class Step1:
    def __init__ (self):
        self.response = 'False'
        self.blackList = BlackList.BlackList().urlListModel.getUrlList()
    
    def getResponse (self, domain:Domain.Domain):
        for url in self.blackList:
            if url.lower() in domain.getDomainNameNetloc():
                domain.setValutation(0,1)
                return True
        return False
            