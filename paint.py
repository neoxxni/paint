import cv2
import mediapipe as mp
import math

mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils
hands=mp_hands.Hands()

camera = cv2.VideoCapture(0)

box_color=(0,255,0)
brush_color=(0,0,255)

point = [{
    "color": brush_color,
    "points": []}]

while True:
    success,frame=camera.read()
    height,width,_=frame.shape
    frame = cv2.flip(frame, 1)

    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

# Drawing the clear box
    x1 = width - 170
    y1 = 20
    x2 = width - 20
    y2 = 120

    cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, -1) 
    cv2.putText(frame, "Clear",(x1 + 25, y1 + 60),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),2)

    cv2.rectangle(frame, (40, 40), (100, 100), (255,0,0), -1) 
    cv2.rectangle(frame, (140,40), (200, 100), (0,255,0), -1) 
    cv2.rectangle(frame, (240, 40), (300, 100), (0,0,255), -1) 

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

#Identification
            index_tip=hand_landmarks.landmark[8]
            index_x=int(index_tip.x*width)
            index_y=int(index_tip.y*height)
            index_fin=(index_x,index_y)

            thumb_tip=hand_landmarks.landmark[4]
            thumb_x=int(thumb_tip.x*width)
            thumb_y=int(thumb_tip.y*height)
            thumb_fin=(thumb_x,thumb_y)

#Appending
            if index_y>130:
                dis2=math.dist(index_fin,thumb_fin)
                if dis2>101:
                    if len(point[-1]["points"])==0:
                        point[-1]["points"].append(index_fin)
                    else:
                        dis1=math.dist(index_fin,point[-1]["points"][-1])
                        if dis1>10:
                            point[-1]["points"].append(index_fin)
                else:
                    if len(point[-1]["points"])!=0:
                        point.append({"color":brush_color,"points":[]})

#Clear button
            if x1 <= index_x <= x2 and y1 <= index_y <= y2:
                box_color = (255, 255, 0) 
                point.clear()
                point.append({"color":brush_color,"points":[]})
            else:
                box_color=(0,255,0)

#Brush color
            if 40 <= index_x <= 100 and  40<= index_y <= 100:
                brush_color=(255,0,0)
            elif 140 <= index_x <= 200 and  40<= index_y <= 100:
                brush_color=(0,255,0)
            elif 240<= index_x <= 300 and  40<= index_y <= 100:
                brush_color=(0,0,255)

#Draw lines
    for stroke in point:
        for i in range(len(stroke["points"])-1):
            cv2.line(frame,stroke["points"][i],stroke["points"][i+1],stroke["color"],5)


#Conclusions
    cv2.putText(frame,"USE INDEX FINGER FOR BRUSH, PINCH TO HOVER",(width//2-400,y1+60),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),5)

    cv2.imshow("Canvas",frame)

    if cv2.waitKey(1)==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()