import cv2  
import numpy as np
  
img = cv2.imread("image.jpg") # Read image 

blurred_img = cv2.GaussianBlur(img, (5, 5), 0)  # Adjust the kernel size if needed
#edge = cv2.Canny(blurred_img, t_lower, t_upper, apertureSize=aperture_size, L2gradient=L2Gradient)
  
# Defining all the parameters
# keep changing the upper and lower parameters for the specific image 
t_lower = 100 # Lower Threshold 
t_upper = 150 # Upper threshold 
aperture_size = 5 # Aperture size 
L2Gradient = True # Boolean 
  
# Applying the Canny Edge filter  
# with Aperture Size and L2Gradient 
edge1 = cv2.Canny(img, t_lower, t_upper, 
                 #apertureSize = aperture_size,  
                 #L2gradient = L2Gradient 
                 ) 

edge2 = cv2.Canny(blurred_img, t_lower, t_upper, 
                 #apertureSize = aperture_size,  
                 #L2gradient = L2Gradient 
                 )  
  
#cv2.imshow('original', img) 
#cv2.imshow('blurred', blurred_img)
cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2) 

kernel = np.ones((3, 3), np.uint8)
dilated_edge = cv2.dilate(edge1, kernel, iterations=1)
eroded_edge = cv2.erode(dilated_edge, kernel, iterations=1)
#cv2.imshow('eroded_edge', eroded_edge)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
edge3 = cv2.Canny(adaptive_threshold, t_lower, t_upper, apertureSize=aperture_size, L2gradient=L2Gradient)
#cv2.imshow('edge3', edge3)

edge0 = cv2.Canny(img, t_lower, t_upper, 
                 apertureSize = aperture_size,  
                 L2gradient = L2Gradient 
                 ) 
#cv2.imshow('edge0', edge0)

cv2.waitKey(0) 
#cv2.destroyAllWindows()