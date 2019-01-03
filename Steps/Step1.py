import Model.Domain as Domain
import Model.BlackList as BlackList
class Step1:
    def __init__ (self):
        self.response = 'False'
        self.blackList = BlackList.BlackList()
    
    def getResponse (self, domain:Domain.Domain):
        self.response = (domain.getBaseUrl() in self.blackList.urlListModel.getUrlList())
        return self.response