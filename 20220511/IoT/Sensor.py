import Adafruit_DHT
def DHT11_TH():
    pin = 21
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    value = [t,h]
    #print(value)
    
    return[str(t),str(h)]
#DHT11_TH()