import cv2
import math

class DrawingTool:
    def __init__(self):
        self.brush_color=(0,0,255)
        self.strokes = [{
    "color": self.brush_color,
    "points": []}]

    def update(self,frame,gesture,landmarks):

        if gesture=="draw":
            if len(self.strokes[-1]["points"])==0:
                self.strokes[-1]["points"].append(landmarks[0])
            else:
                dis1=math.dist(landmarks[0],self.strokes[-1]["points"][-1])
                if dis1>10:
                    self.strokes[-1]["points"].append(landmarks[0])

        if gesture=="pinch":
            if len(self.strokes[-1]["points"])!=0:
                self.strokes.append({"color":self.brush_color,"points":[]})

        if gesture=="select_blue":
            self.brush_color=(255,0,0)
        if gesture=="select_green":
            self.brush_color=(0,255,0)
        if gesture=="select_red":
            self.brush_color=(0,0,255)
        if gesture=="clear":
            self.strokes.clear()
            self.strokes.append({"color":self.brush_color,"points":[]})


    def show(self,frame):
        for stroke in self.strokes:
            for i in range(len(stroke["points"])-1):
                cv2.line(frame,stroke["points"][i],stroke["points"][i+1],stroke["color"],5)