import datetime
from datas import Datas
from random import choice


def IntroduceItself():
    Conversion = Datas.IntroConversation.get("intro")
    return Conversion



def Wish() -> str :
    hour = datetime.datetime.now().strftime("%H")
    if( int(hour) > 10 and int(hour) < 12 ):
        return choice(Datas.wish.get("morning"))
    
    if( int(hour) > 12 and int(hour) < 17 ):
        return choice(Datas.wish.get("afternoon"))
    
    if( int(hour) > 17 and int(hour) < 20 ):
        return choice(Datas.wish.get("evening"))
    
    if( int(hour) > 20 and int(hour) < 10):
        return choice(Datas.wish.get("night"))
    
def GetTimeDtae():
    hour = datetime.datetime.now().strftime("%H%M%S")
    print(hour)
