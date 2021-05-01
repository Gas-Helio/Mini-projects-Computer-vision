import cv2
import mediapipe as mp


class HandTraking:
    def __init__(self, tracking_confi=.5, detection_confi=.5, max_hands=1):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            min_tracking_confidence=tracking_confi,
            min_detection_confidence=detection_confi,
            max_num_hands=max_hands)

    def find_position(self, image, my_hand=0, draw=False):
        results = self.hands.process(image)
        h, w, c = image.shape
        position = []
        if results.multi_hand_landmarks:
            position.append([])
            for handLms in results.multi_hand_landmarks:
                if draw:
                    zs = [lm.z for lm in handLms.landmark]
                    z_max, z_min = max(zs), min(zs)
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
                for id_, lm in enumerate(handLms.landmark):
                    cx, cy = int(w * lm.x), int(h * lm.y)
                    position[-1].append((cx, cy, lm.z))
                    if draw:
                        z = (lm.z - z_min) / (z_max - z_min)
                        cv2.circle(image, (cx, cy), 5, (int((1 - z) * 255), 0, int(z * 255)), thickness=-1)
        if draw:
            return position, image
        return position
