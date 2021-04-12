import cv2 as cv
import numpy as np


class Angle:
    def __init__(self, path):
        self.img = cv.imread(path)
        if max(self.img.shape) > 1366:
            self.img = cv.resize(self.img, (int(self.img.shape[1] * .5), int(self.img.shape[0] * .5)))
        self.points = []

    def getAngle(self):
        p1, p2, p3 = self.points

        p21 = [p2[0] - p1[0], p2[1] - p1[1]]
        p31 = [p3[0] - p1[0], p3[1] - p1[1]]

        cosine_angle = np.dot(p21, p31) / (np.linalg.norm(p21) * np.linalg.norm(p31))
        angulo = np.degrees(np.arccos(cosine_angle))

        cv.putText(self.img, str(round(angulo)), tuple(p3), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    def getPositionMouse(self, event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            self.points.append([x, y])
            cv.circle(self.img, tuple(self.points[-1]), 5, (0, 0, 255), -1)
            if len(self.points) > 1:
                cv.line(self.img, tuple(self.points[0]), (x, y), (0, 0, 255), 3)
            if len(self.points) >= 3:
                self.getAngle()
                self.points = []
    def run(self):
        while True:
            cv.imshow('Aperte q para sair', self.img)
            cv.setMouseCallback('Aperte q para sair', self.getPositionMouse)

            if cv.waitKey(20) & 0xff == ord('q'):
                break

        cv.destroyAllWindows()


if __name__=='__main__':
    a = Angle('images/protractor.jpg')
    a.run()
