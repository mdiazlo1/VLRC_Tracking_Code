import cv2 as cv
def rescaleFrame(frame,scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

def BoundaryTracks(contour):
    #This will reshape the contour array to just be a 2D array with all positions
    New_cnt = cnt.reshape(cnt.shape[0],2)
    
    
    Newnew_cnt = np.zeros((New_cnt.shape[0],New_cnt.shape[1],total),dtype = 'int32')
    Newnew_cnt[:,:,1] = cnt.reshape(cnt.shape[0],2)
    



