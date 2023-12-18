import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

dht_pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature={temperature:.1f}*C  Humidity={humidity:.1f}%')
    else:
        print('Failed to get reading. Try again!')
    
    time.sleep(2)
