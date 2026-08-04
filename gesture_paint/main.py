import hand_tracker
import gesture_identifier
import drawing_tool
import ui
import cv2

tracker=hand_tracker.HandTracker()
recognizer=gesture_identifier.GestureRecognizer()
draw=drawing_tool.DrawingTool()
interface=ui.UI()

camera=cv2.VideoCapture(1)

while True:
    success,frame=camera.read()
    frame=cv2.flip(frame,1)

    interface.canvas(frame)

    landmarks=tracker.detect(frame)
    board=draw.show(frame)

    if landmarks is not None:
        gesture=recognizer.detect(frame,landmarks)
        canvas=draw.update(frame,gesture,landmarks)

    cv2.imshow("Canvas",frame)
    if cv2.waitKey(1)==ord('q'):
            break
    
camera.release()
cv2.destroyAllWindows()