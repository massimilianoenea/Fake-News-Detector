import Model.Domain as urlDomain
import Steps.Step1 as step1
import Steps.Step2 as step2
import Model.ArticleParsed as article

domain = urlDomain.Domain("http://aprilamente.info/non-si-puo-fermare-cio-che-sta-arrivando/")
firstStep = step1.Step1()
secondStep = step2.Step2()
print("Avvio il Primo step")
isInBlackList = firstStep.getResponse(domain)
if(isInBlackList):
    print("Primo step ultimato")
print("Avvio il Secondo step")
variabile = secondStep.checkRefToOtherSite(domain)
if(len(variabile) > 0):
    #qui devo aggiungere il codice per salvare i nuovi link nella blacklist
    #print(variabile)
    print("Secondo step ultimato")
print("Avvio il Terzo step")
parsedArticle = article.ArticleParsed(domain)
if(parsedArticle.isValidUrl):
    print(parsedArticle.title)
    #print(parsedArticle.summary)
    #print(parsedArticle.keywords)
    print("Terzo step ultimato")

finalValutation = 0

for valutation in domain.valutation:
    finalValutation += valutation

print((finalValutation/2)*100)
print(domain.valutation)