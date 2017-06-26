import picamera

cam = picamera.PiCamera()

try:
    print("Starting Camera Recording")
    cam.start_preview()
    cam.start_recording('/home/pi/Desktop/cam_record.h264')
    while True:
        pass
except:
    print("Stopping Camera Recording")
    cam.stop_recording()
    cam.stop_preview()
    cam.close()
