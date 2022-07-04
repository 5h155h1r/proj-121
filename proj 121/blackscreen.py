import cv2
import numpy as np


vidcap = cv2.VideoCapture(0)
img = cv2.imread("new.jpg")

while True:
    ret, frame = vidcap.read()
    print(frame)
    frame = cv2.resize(frame, (640, 480))
    img = cv2.resize(img, (640, 480))
    u_black = np.array([255, 0, 0])
    l_black = np.array([30, 30, 0])
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame - res 
    f = np.where(f==0, img, f)
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

vidcap.release()
cv2.destroyAllWindows()
