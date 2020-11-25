#get warp perspective on an image to get a bird eye's view of it

import cv2
import numpy as np

image_path = cv2.imread("resources/cards.jpg") #image from Git repo - Murtaza Workshop YT

#A playing card is usually 2.5 by 3.5 inches, so we are maintaining the ratio here.
width, height = 250, 350

#using np.float32 since we need a floating point array.
#defines the 4 set of points/ 4 corner points of an object in an image you want to capture and warp i.e King of Spades in this case.
#You can get these points easily in MS Paint software and cursor the points you want in an image.
points1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]]) 

#for each of those points above, we need to define which corner are we referring to.
#example: is the first point origin above in the top left-hand corner or is the last point origin
#in the bottom right corner? etc. We need to define each point origin above with each corner.
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]]) 

#transformation matrix required for the perspective itself
'''
getPerspectiveTransform(points1, points2) - 
	Calculates a perspective transform from four pairs of the corresponding points. 
	Coordinates of quadrangle vertices in the source image  (object in an src image). 
	Coordinates of the corresponding quadrangle vertices in the destination image.
'''
matrix = cv2.getPerspectiveTransform(points1, points2) #transforming an image to another based on a perspective.

#get the output image based on the matrix above. Warp the object in the src image with the matrix above.
#warpPerspective(src image, matrix, dSize)
image_output = cv2.warpPerspective(image_path, matrix, (width, height))

cv2.imshow("Image", image_path)
cv2.imshow("Warped image", image_output)

cv2.waitKey(0)