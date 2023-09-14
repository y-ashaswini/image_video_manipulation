import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import time


fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
font = cv2.FONT_HERSHEY_DUPLEX

def nothing(x):
    pass

cv2.namedWindow("hello")
cv2.createTrackbar("quality","hello",1,100,nothing)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    cap.open(1)

if cap.isOpened():
    while(cap.isOpened()):
        ret, frame = cap.read()

        frame =cv2.flip(frame, -1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([0, 0, 200])
        upper_green = np.array([180, 255, 255])
        # lower_green = np.array([59,90,151])
        # upper_green = np.array([83,255,255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        blur = cv2.GaussianBlur(mask,(9,9),0)     
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY) 
        

        quality = cv2.getTrackbarPos("quality","hello")   
        quality = quality/100
        corners = cv2.goodFeaturesToTrack(image=blur,maxCorners=5,qualityLevel=quality, minDistance=10)

        if(corners is None): continue

        corners = np.int0(corners)
        for i in corners:
            x,y = i.ravel()
            cv2.circle(frame,(x,y),10,(0,0,255),-1)
        cv2.imshow('hello', frame)


        for i in corners[0]:
            a0=i[0]
            b0=i[1]
        for i in corners[1]:
            a1=i[0]
            b1=i[1]
        for i in corners[2]:
            a2=i[0]
            b2=i[1]
        for i in corners[3]:
            a3=i[0]
            b3=i[1]
        for i in corners[4]:
            a4=i[0]
            b4=i[1]

        am=(a0+a1)/2
        bm=(b0+b1)/2
        print(am,bm)

        contours, hier = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)   



        for c in contours:
            # find minimum area
            x,y,w,h = cv2.boundingRect(c)
            (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,center,radius,(0,255,0),2)
            cv2.circle(frame,center,2,(0,255,0),2)
            cv2.circle(frame,(int(am),int(bm)),2,(0,255,0),2)       


        cv2.line(frame,center,(int(am),int(bm)),(255,0,0),1)
        cv2.line(frame,center,(int(radius+x),int(y)),(255,0,0),1)
        
        #Angles
        atan=math.atan2(int(bm)-int(y),int(am)-int(x))
        angle=math.degrees(atan)
        print ('angle=', angle)
        if(angle >= -45 and angle < 45):
            cv2.putText(frame,'RIGHT',(10,85),font,1,(255,255,0))
            print("RIGHT")
        elif(angle >=45 and angle < 135):
            cv2.putText(frame,'DOWN',(10,85),font,1,(255,255,0))
            print("DOWN")
        elif(angle >= -180 and angle <=-135): 
            cv2.putText(frame,'LEFT',(10,85),font,1,(255,255,0))
            print("LEFT")
        elif(angle >=135 and angle <=180):
            cv2.putText(frame,'LEFT',(10,85),font,1,(255,255,0))
            print("LEFT")
        elif(angle > -135 and angle < -45):
            cv2.putText(frame,'UP',(10,85),font,1,(255,255,0))
            print("UP")

    #### SHOWING AND SAVING THE OUTPUT
        cv2.imshow('hello',frame)
        b = cv2.resize(frame, (1280,720), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC) 

        k = cv2.waitKey(1)
        # press esc to end.
        if k == 27:
            print("exiting.")
            break;


    cap.release()
    cv2.destroyAllWindows()

        
