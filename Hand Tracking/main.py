import cv2
import time
from HandTracking import HandTraking

cap = cv2.VideoCapture(1)
oTime = time.time()
hands = HandTraking(tracking_confi=.6, detection_confi=.5, max_hands=1)

while True:
    _, frame = cap.read()
    # frame = cv2.resize(frame, (int(frame.shape[1]*.75), int(frame.shape[0]*.75)))
    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    _, image = hands.find_position(frame, draw=True)

    dTime = time.time()
    fps = 1/(dTime - oTime)
    oTime = dTime

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.putText(frame, f'FPS: {round(fps, 2)}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow('cam', frame)

    if cv2.waitKey(20) & 0xff == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()
