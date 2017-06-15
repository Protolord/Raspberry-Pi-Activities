import pigpio
import DHT22
import time

pi = pigpio.pi()
s = DHT22.sensor(pi, 4)

try:
    print("Program starting")
    while True:
        s.trigger()
        print("humidity = ", s.humidity())
        print("temperature = ", s.temperature())
        time.sleep(1.0)
except:
    print("Program terminating")
    s.cancel()
    pi.stop()

