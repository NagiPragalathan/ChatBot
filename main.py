from Processes.MainFunctions import (init, speak, Input, WebScrap,scrping)
from Processes.CommonRespons import IntroduceItself
from datas.Normal import NormalConverstation

# variables

CurrentFeeling = "Happy"
CurrentLanguage = "en"

# wake up
OrderSilent = False

# Runing Loop
Life = True

OneTimeCodes = True

while Life:
    if OneTimeCodes :
        OneTimeCodes = False
        init()
    
    FetchingLines = 2
    
    # Get Input From User
    responce = Input(CurrentLanguage)
    print(responce)
    
    # Normal Converstation Using Json Datas
    FetchFromOffline = NormalConverstation(responce)
    
    if FetchFromOffline :
        speak(FetchFromOffline, CurrentLanguage)
    else:
        # Scrping the Datas from Web
        FetchingTry1 = WebScrap(responce,FetchingLines)
        if FetchingTry1 :
            speak(FetchingTry1,CurrentLanguage)
        else :
            speak(scrping(responce,FetchingLines),CurrentLanguage)
        
        
        
        