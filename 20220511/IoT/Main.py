import FunC as uf
import Sensor as us
import os
import sys

myRow=[] 

#"自訂" = uf.My_Name() 
#"自訂" = uf.My_MAC()
#"自訂" = uf.My_Date()
#"自訂" = uf.My_Time()
#"自訂" = uf.My_IP()

#"自訂" = us.DHT11_TH()
def Get_Data():
    Room_Number = uf.My_Name() #HOST-NAME = 房號
    Remote_IP = uf.My_IP()
    #Remote_IP = "測試IP"
    Date = uf.My_Date()
    Time = uf.My_Time()
    S1= us.DHT11_TH()   #傳感器資訊
    #S2= us.DHT11_TH()
    #S1= "測試溫度"   #傳感器資訊
#    myRow=[str(Room_Number[0]),str(Remote_IP[0]),str(Date[0]),str(Time[0]),str(S1[0]),str(S2[0])]
    myRow=[str(Room_Number[0]),str(Remote_IP[0]),str(Date[0]),str(Time[0]),str(S1[0]),str(S1[1])]
    #print(myRow)

    return [myRow]

Get_Data()