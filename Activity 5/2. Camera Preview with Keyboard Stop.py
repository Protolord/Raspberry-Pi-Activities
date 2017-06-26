import picamera

cam = picamera.PiCamera()

try:
    print("Starting Camera Preview")
    cam.start_preview()
    while True:
        pass
except:
    print("Stopping camera")
    cam.stop_preview()
    cam.close()

