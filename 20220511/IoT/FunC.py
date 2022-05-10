'''
說明:
硬體設備相關資訊
*自訂義功能函式
*更新日期:2021-12-22
*
'''
from time import*
import time
import uuid #抓MAC
import os
import socket #抓IP

#########################
#    取得設備相關資訊
#########################

def My_Name():
    value = socket.gethostname()
    #print(value)
    
    return [value]

def My_MAC():
    value = uuid.UUID(int =uuid.getnode()).hex[-12:]
    #print(value)
    
    return [value]

def My_Date():
    value = time.strftime("%Y-%m-%d", time.localtime())
    #print(value)
    
    return [value]

def My_Time():
    value = time.strftime("%H:%M", time.localtime())
    #print(value)
    
    return [value]

def My_IP():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        value = s.getsockname()[0]
        
        #print(value)
        return [value]



#########################
#    執行單一功能
#########################

def My_All():
    My_Name()
    My_MAC()
    My_Date()
    My_Time()
    My_IP()  #LINUX環境使用
    
    
My_All()