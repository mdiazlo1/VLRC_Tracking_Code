import cv2 as cv; import numpy as np
import Functions as fn

video = cv.VideoCapture("..\Blue Origin Videos\EC-Bottom-GX010142 - Trim.MP4")

total = int(video.get(cv.CAP_PROP_FRAME_COUNT)); res,frame = video.read()
ImgBg = frame

def contourFilter(contour):
    Area = cv.contourArea(contour)
    return Area

start_number = 0
video.set(cv.CAP_PROP_POS_FRAMES,start_number-1)
for Frame_Num in range(start_number,total):
    isTrue, frameOrig = video.read()
    
    #Remove the background from the image
    frame = cv.subtract(frameOrig, ImgBg)
    blank = np.zeros(frame.shape,dtype = 'uint8')
    #Convert image to greyscale
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY); 
    #Apply a guassian blur to take out some noise
    frame = cv.GaussianBlur(frame, (7, 7), 5) 
    #Enhance contrast and brightness
    frame = cv.convertScaleAbs(frame, alpha=10, beta=10)

    #Sharpen the image; This ended up not helping too much for the video I was working with.
    #kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) #sharpening kernel
    #frame = cv.filter2D(frame, -1, kernel) 
  
    #binarize and invert the image
    thresh,frame = cv.threshold(frame,10,255,cv.THRESH_BINARY_INV)
    #frame = cv.bitwise_not(frame)
    edges = cv.Canny(frame,50,240)
    
    #Contour finder and draws contours on the blank image we created earlier
    contours, hierarchies = cv.findContours(frame,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    
    #Let's filter the contours so we don't have the noisy ones
    contours_filt = list(filter(lambda x: cv.contourArea(x)>2000, contours))
    
    #Now draw the contours on the original image so we can visualize it with the data
    cv.drawContours(frameOrig, contours_filt,-1, (0,0,255), 3) 
    
    #after filtering for GX010034_1693593667530.MP4 look at contour 2 to figure out velocity
    
    
    #Use the code below if you want to view the video as it loops through. 
    #Press "d" on your keyboard when you want it to stop.
    frame_resized = fn.rescaleFrame(frame); blank_resized = fn.rescaleFrame(frameOrig)
    cv.imshow('Video',frame_resized)
    cv.imshow('Contours',blank_resized)
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
    
video.release()
cv.destroyAllWindows()



























