#Draw contour on blank image so we know which one we are working with
'''blank = np.zeros(frameOrig.shape,dtype = 'uint8')
cv.drawContours(blank, contours_filt,2, (0,0,255), 3)
blank = fn.rescaleFrame(blank)
cv.imshow('contours',blank)
cv.waitKey(0)
cv.destroyAllWindows()'''
import matplotlib.pyplot as plt

cnt = contours_filt[1]
New_cnt = cnt.reshape(cnt.shape[0],2)
plt.imshow(frameOrig)
plt.scatter(New_cnt[:,0],New_cnt[:,1])




#plt.xlim(0,frame.shape[1])
#plt.ylim(0,frame.shape[0])




