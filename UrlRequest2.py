import Model.Domain as urlDomain
import Steps.Step1 as step1
import Steps.Step2 as step2

domain = urlDomain.Domain("http://aprilamente.info")
firstStep = step1.Step1()
secondStep = step2.Step2()
print(firstStep.getResponse(domain))
print(secondStep.checkRefToOtherSite(domain))
print(domain.getBaseUrl())
