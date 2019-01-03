import Model.UrlList as UrlList

class ExcludeList():
    def __init__(self):
        self.urlListModel = UrlList.UrlListModel("./UrlList/excludeList.txt")