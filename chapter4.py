#draw shapes (lines, rectangles, circles etc) and add text on images

import cv2
import numpy as np

#create a matrix with just Zeros. Zero in open cv means black. Ones are white
#This is a greyscale image due to its size. If you want to add a color fn.ality you need to provide
# '3' channels i.e BGR
image = np.zeros((512, 512, 3), np.uint8)
# print(image)

#add color to the image above. image[:] means for the whole image or you can
#set the height and width respectively and color that specified area in the image.
image[100:200, 100:200] = 51, 0, 0

#create a line in an image - 
#cv2.line(image, starting point (w:h), ending point (w:h), line color, optional: thickness)

#cv2.line(image, (0,0), (300, 300), (255,255,255), 200)

#create a line till the end of the image
cv2.line(image, (0,0), (image.shape[1], image.shape[0]), (255,255,255), 2)

#create a rectangle in an image
#same like above function - width and height respectively
# cv2.rectangle(image, (0,0), (250,350), (102,204,0), 3) #OR to fill the shape/thickness, you can use cv2.FILLED
cv2.rectangle(image, (0,0), (250,350), (102,204,0), cv2.FILLED)

#create a circle in an image 
#cv2.circle(image, centre point of circle (w:h), radius, color, thickness)
cv2.circle(image, (400, 50), 5, (0,255,0), 2)

#place text on an image
#cv2.putText(image, define text, starting point origin, define text font, scale, color, thickness)
cv2.putText(image, "OPEN CV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1.4, (130, 25, 0), 3)


cv2.imshow("Image", image)

cv2.waitKey(0)

