#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#開發人員:Ness_huang
#日期:2021-11-05
#版本號:v1
#
#全域變數global variable
TEMP_01=0; HUMI_01=0; TEMP_02=0; HUMI_02=0;
Oid_list = "TEMP_01/HUMI_01/TEMP_02/HUMI_02"
                       
def __Original_SNMP__():
    import time
    import board  
    import psutil
    import Adafruit_DHT
    global TEMP_01,HUMI_01,TEMP_02,HUMI_02

###kill processing
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    
    pin = 21
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    sensor1 = [t,h]
    #print(sensor1[0],sensor1[1])
    
###GPIO pin
    #pin = 22
    #h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    #sensor2 = [t,h]
    #print(sensor2[0],sensor2[1])

    TEMP_01 = sensor1[0]
    HUMI_01 = sensor1[1]

    __CreatNewFile__()
    __EditFile__()

#產生oid-value.py
def __CreatNewFile__():
    print("__CreatNewFile__() - 用於產生oid-value.py")
    from pathlib import Path

    myfile = Path('oid-value.py')
    myfile.touch(exist_ok=True)
    f = open(myfile)

def __EditFile__():
    print("__EditFile__() - 用於更新oid-value.py內文")
    path = 'oid-value.py'
    f = open(path, 'w')
    f.write("print('{}')\n".format(Oid_list))
    f.write("print('{0:0.0f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    f.write("print('{1:0.0f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    #f.write("print('{2:0.0f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    #f.write("print('{3:0.0f}')\n".format(TEMP_01, HUMI_01, TEMP_02, HUMI_02))
    
    f.close()
        
__Original_SNMP__()    