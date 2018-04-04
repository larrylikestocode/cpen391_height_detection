import time
import picamera
import sys
print(sys.argv[1])
camera = picamera.PiCamera()
camera.resolution =(1600,700)
camera.start_preview()
file_header = "photos/"
file_footer = ".jpg"
file_name = sys.argv[1]
time.sleep(5)
camera.capture(file_header+file_name+file_footer)
camera.stop_preview()
