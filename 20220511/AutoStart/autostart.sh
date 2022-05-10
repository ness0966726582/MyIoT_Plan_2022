#!/bin/bash
echo "power on time:$(date '+%c')" >> /home/pi/log.txt
cd /home/pi/Desktop/IoT
nohup python3 Update.py


echo "System-Time-not-Enough recommand  " >> /home/pi/log.txt
echo "[ pi@XXXX:~ $ sudo nano /etc/rc.local] + [sleep 10]" >> /home/pi/log.txt