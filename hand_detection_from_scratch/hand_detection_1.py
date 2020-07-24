import cv2
import numpy as np
import pyautogui
import time
cap = cv2.VideoCapture(1)
hand_cascade = cv2.CascadeClassifier('hand.xml')
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    sum = 0
    for (x, y, w, h) in hand:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        sum = sum+1
    cv2.imshow('Frame', frame)
    if(sum == 1):
        print("hand fist detected")
    else:
        print("hand fist not detected")
        #pyautogui.press('space')
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break		
cap.release()
cv2.destroyAllWindows()
