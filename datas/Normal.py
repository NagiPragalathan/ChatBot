from Processes.MainFunctions import WebScrap


WebScrapKeys = ["what","define"]

def NormalConverstation(responce : str) :
    
    for i in WebScrapKeys:
        if(i in responce):
            return False
        