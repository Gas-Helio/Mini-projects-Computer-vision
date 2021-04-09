import cv2 as cv
import numpy as np


def getAngle(points):
    p1, p2, p3 = points

    p21 = [p2[0] - p1[0], p2[1] - p1[1]]
    p31 = [p3[0] - p1[0], p3[1] - p1[1]]

    cosine_angle = np.dot(p21, p31) / (np.linalg.norm(p21) * np.linalg.norm(p31))
    angle = np.degrees(np.arccos(cosine_angle))

    print(p1)
    cv.putText(img, str(round(angle)), tuple(p3), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)


points = []
def getPositionMouse(event, x, y, flags, params):
    global points
    if event == cv.EVENT_LBUTTONDOWN:
        points.append([x, y])
        cv.circle(img, tuple(points[-1]), 5, (0, 0, 255), -1)
        if len(points) > 1:
            cv.line(img, tuple(points[0]), (x, y), (0, 0, 255), 3)
        if len(points) >= 3:
            getAngle(points)
            points = []


img = cv.imread('images/protractor.jpg')
img = cv.resize(img, (int(img.shape[1]*.3), int(img.shape[0]*.3)))
while True:
    cv.imshow('Image', img)
    cv.setMouseCallback('Image', getPositionMouse)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

cv.destroyAllWindows()