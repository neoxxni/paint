import cv2

class UI:
    def __init__(self):
        self.box_color=(0,255,0)

    def canvas(self,frame):
        height,width,_=frame.shape
        cv2.putText(frame,"USE INDEX FINGER FOR BRUSH, PINCH TO HOVER",(width//2-400,80),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),5)
        cv2.rectangle(frame, (width - 170, 20), (width - 20, 120), self.box_color, -1) 
        cv2.putText(frame, "Clear",(width - 145, 80),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),2)
        cv2.rectangle(frame, (40, 40), (100, 100), (255,0,0), -1) 
        cv2.rectangle(frame, (140,40), (200, 100), (0,255,0), -1) 
        cv2.rectangle(frame, (240, 40), (300, 100), (0,0,255), -1) 

    def highlight_button(self):
            self.box_color=(255,255,0)

