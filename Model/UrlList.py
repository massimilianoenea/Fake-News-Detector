class UrlListModel:
    def __init__(self, file):
        fileRead = open(file, 'r')
        self.listOfUrl = []
        for line in fileRead.read().splitlines():
            self.listOfUrl.append(line)

    def getUrlList (self):
        return self.listOfUrl

    def setNewUrl (self, url):
        self.listOfUrl.append(url)
