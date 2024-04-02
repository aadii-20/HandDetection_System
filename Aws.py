import cv2
from cvzone.HandTrackingModule import HandDetector
import os

cap = cv2.VideoCapture(0)
status, photo = cap.read()

cv2.imshow("Aditya-Photo",photo)
cv2.waitKey()
cv2.destroyAllWindows()

cap.release()
# By this code we can click the photo by code

cap = cv2.VideoCapture(0)
while True:
    status, photo = cap.read()
    cv2.imshow("Aditya-Photo",photo)
    if (cv2.waitKey(10) == 13):
        break
    cv2.destroyAllWindows()

cap.release()
# By this code we can do the live stream by python code 

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector()
cap = cv2.VideoCapture(0)
status, photo = cap.read()

hand = detector.findHands(photo, draw=True)

hand

cv2.imshow("Aditya Hand's", photo)
cv2.waitKey()
cv2.destroyAllWindows()

cap.release()
# By that code we can check our hand its right or left by python code

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1,detectionCon=0.8)
cap = cv2.VideoCapture(0)

status, photo = cap.read()

hand = detector.findHands(photo,draw=False)

cap.release()

import os
import cv2  # Make sure to import necessary libraries

def fingerG():
    cap = cv2.VideoCapture(0)  # Initialize the camera capture

    while True:
        status, photo = cap.read()
        # photo = cv2.flip(photo, 1)
        hand = detector.findHands(photo, draw=False)  # Make sure 'detector' is properly defined
        # find = cv2.imread("Put image ")
        cv2.imshow("Aditya-Photo", photo)

        if cv2.waitKey(1) == 13:
            break

        fingersup = [0, 0, 0, 0, 0]  # Initialize the 'fingersup' list

        if hand:
            lm = hand[0]
            if lm:
                fingersup = detector.fingersUp(lm)

        if fingersup == [0, 1, 0, 0, 0]:
            os.system("notepad")
            fingerG()
        if fingersup == [0, 1, 1, 0, 0]:
            os.system("mspaint")
            fingerG()
        if fingersup == [0, 1, 1, 1, 0]:
            os.system("explorer")
            fingerG()
        if fingersup == [0, 1, 1, 1, 1]:
            os.system("ms-photos")
            fingerG()
        if fingersup == [1, 1, 1, 1, 1]:
            break
        
            # Do something for all fingers up
            # You need to define the action you want to take here
    cv2.waitKey()
    cv2.destroyAllWindows()
    cap.release()
status, photo = cap.read()
cv2.imshow("Aditya-Photo", photo)
cap.release()
cv2.destroyAllWindows()

# Call the function


fingerG()

cap.release()
