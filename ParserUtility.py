import base64
import numpy as np
from datetime import datetime
import cv2
def parseImage(img):
 currentImage = base64.b64decode(img);
 nparr = np.fromstring(currentImage, np.uint8)
 img_np = cv2.imdecode(nparr, 1)
 ret, jpegImage = cv2.imencode('.jpg', img_np)
 return jpegImage.tobytes()


def buildFileName(createdDate, deviceName):
     date_time = createdDate.strftime("%m:%d:%Y-%H:%M:%S")
     return deviceName+"/"+date_time
