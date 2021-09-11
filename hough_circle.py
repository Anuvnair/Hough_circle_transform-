import numpy as np
import cv2

lower = np.array([0,60,80])
upper = np.array([20,140,250])
frame = cv2.imread('F3.png')

hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))



dil = cv2.dilate(mask, kernel, iterations=1)
cv2.imshow('blah',dil)

gradient = cv2.morphologyEx(dil, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('bl',gradient)

circles = cv2.HoughCircles(gradient,cv2.HOUGH_GRADIENT,1,45,
                            param1=50,param2=30,minRadius=0,maxRadius=140)
circles = np.uint16(np.around(circles))
print circles
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
#Display the detected circle(s):
cv2.imshow('detected circles',frame)
#Wait for the user to exit the program
cv2.waitKey(0)
cv2.destroyAllWindows()


