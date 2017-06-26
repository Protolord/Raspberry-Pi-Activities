import picamera
import time

cam = picamera.PiCamera()
cam.start_preview()
time.sleep(5)
cam.stop_preview()
cam.close()
