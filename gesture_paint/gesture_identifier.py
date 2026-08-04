import cv2
import math

class GestureRecognizer:
    def __init__(self):
        pass

    def detect(self,frame,landmarks):
        height,width,_=frame.shape
        dist1=math.dist(landmarks[0],landmarks[1])
        if 40 <= landmarks[0][0] <= 100 and  40<= landmarks[0][1] <= 100:
            return "select_blue" 
        if 140 <= landmarks[0][0] <= 200 and  40<= landmarks[0][1] <= 100:
            return "select_green"
        if 240<= landmarks[0][0] <= 300 and  40<= landmarks[0][1] <= 100:
            return "select_red"
        
        if width-170 <= landmarks[0][0] <= width-145 and 20 <= landmarks[0][1] <= 120:
            return "clear"
        else:
            pass
        
        if dist1>101:
            if landmarks[0][1]>130:  #index_fin landmark y
                return "draw"
        else:
            return "pinch"