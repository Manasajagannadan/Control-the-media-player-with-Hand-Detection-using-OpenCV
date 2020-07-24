import cv2
import numpy as  np 
import pyautogui
import time
ct=0
ct1=0
time.sleep(5)
cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('palm.xml')
while(True):
    ret, frame = cap.read()
    print(type(cap))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    if len(hand) == 0:
        print ("No hand found")
    else:
        sum = 0
        print("detecting the number of hands")
        for (x,y,w,h) in hand:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            sum = sum+1
            #print("frame:", len(frame))
            if len(frame) > 0:
                pyautogui.press('space')
                print("1")
                sum = 1
            else:
                pass
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()