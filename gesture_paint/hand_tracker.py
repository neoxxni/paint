import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands=mp.solutions.hands
        self.mp_draw=mp.solutions.drawing_utils
        self.hands=self.mp_hands.Hands()

    def detect(self,frame):
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(rgb)
        if not results.multi_hand_landmarks:
            return None
        for hand_landmarks in results.multi_hand_landmarks:
            self.mp_draw.draw_landmarks(frame,hand_landmarks,self.mp_hands.HAND_CONNECTIONS)
            index_fin=self._track(8,frame,hand_landmarks)
            thumb_fin=self._track(4,frame,hand_landmarks)
            return(index_fin,thumb_fin)

    def _track(self,number,frame,hand_landmarks):
        height,width,_=frame.shape
        fin_loc=hand_landmarks.landmark[int(number)]
        fin_x=int(fin_loc.x*width)
        fin_y=int(fin_loc.y*height)
        fin=(fin_x,fin_y)
        return fin
