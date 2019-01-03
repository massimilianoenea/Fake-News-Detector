import Model.UrlList as UrlList

class BlackList():
    def __init__(self):
        self.urlListModel = UrlList.UrlListModel("./UrlList/blackList.txt")