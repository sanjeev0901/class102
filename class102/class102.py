from cgitb import reset
from unittest import result
import cv2

def takeSnapshot():
    videoCaptureObject = cv2.VideoCapture(0);
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("D:/Sanju/WhiteHatJr/Python Classes/class102/newImage1.png",frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
takeSnapshot()