import numpy as np
import cv2

# Read the image and convert to greyscale
img = cv2.imread('assets/corners.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# Find the top 20 corners using the cv2.goodFeaturesToTrack()
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)

# Iterate over the corners and draw a circle at that location
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),5,(0,0,255),-1)
    
# Display the image
cv2.imshow('a', img)
cv2.waitKey(0)