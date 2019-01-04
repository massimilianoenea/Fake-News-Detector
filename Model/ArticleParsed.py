from newspaper import Article
import Model.Domain as Domain

class ArticleParsed:
    def __init__ (self, domain:Domain.Domain):
        url = domain.getArticleUrl()
        self.articleUrl = url
        article = Article(url,language='it')
        self.isValidUrl = article.is_valid_url()
        if(article.is_valid_url()):
            article.download()
            article.parse()
            self.title = article.title
            self.author = article.authors
            self.publish_date = article.publish_date
            self.text = article.text
            self.tags = article.tags
            article.nlp()
            self.summary = article.summary
            self.keywords = article.keywords

    def getArticleTitle (self):
        return self.title

    def getArticleSummary (self):
        return self.summary
    
    def getArticleKeywords (self):
        return self.keywords