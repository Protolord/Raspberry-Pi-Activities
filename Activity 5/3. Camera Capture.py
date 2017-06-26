import picamera

cam = picamera.PiCamera()

try:
    print("Starting Camera Preview")
    cam.start_preview()
    while True:
        pass
except:
    print("Capturing Image")
    cam.capture('/home/pi/Desktop/cam_image.jpg')
    cam.stop_preview()
    cam.close()
