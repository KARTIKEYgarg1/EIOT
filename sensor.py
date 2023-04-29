import Adafruit DHT
import time
import RPi.GPIO as GPIO
DHT SENSOR = Adafruit DHT.DHT11
DHT PIN = 4

GPI0.setmode (GPI0. BCM)
GPIO.setwarnings (False)
GPI0.setup(2, GPIO.0UT)
GPTO.setup (26, GPI0.IN)
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
        if temperature>=35:
            print("FOUND SOMETHING: ",(1-GPIO.input(26)))
            print("TEMPERATURE EXCEEDED")
            GPIO.output(2,GPIO.HIGH)
        else:
            GPIO.output(2,GPIO.LOW)
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);
