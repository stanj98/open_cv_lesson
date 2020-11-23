#basic functions utilized often when using open CV for projects
import cv2
import numpy as np #deals with matrices

img = cv2.imread('resources/admin.png')

#Function 1: cv2.cvtColor()

#convert image to a greyscale image. cvtColor() converts an image to different color spaces.
#By convention, open cv recognizes the image channel as BGR instead of RGB.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Functon 2: cv2.GaussianBlur(original or grey image above to blur, 
#kernel size - this should contain odd numbers only, sigmaX value)

#blur an image.
imgBlur = cv2.GaussianBlur(imgGray, (3,99), 0)

#Function 3: cv2.Canny(image, threshold value 1, threshold value 2)

#find the number of edges using the Canny edge detector function.
imgCanny = cv2.Canny(img, 150, 200)

#Function 4: cv2.dilate(unclear edge image i.e Canny image, kernel size - a matrix that needs to define
#the size and the value of. 
#In this case, we need a matrix that has all ones-values and the size as well, define the number
#of iterations we need the kernel to move around i.e how much thickness do we actually need)

#Library that deals with matrices powerfully and efficiently: Numpy

#increase the thickness of the edges since there might be a gap or it might not be joined properly.
#It will not detect it as a proper line therefore we use the dilation method to increase the edge thickness.

#define a kernel :
#ones() - all the values will be ones. 
#size of the matrix i.e 5 by 5 in this case.
#type of the object i.e unsigned (only positive integer values) with 8 bits (0-255). 
kernel = np.ones((5,5), np.uint8)

imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)

#Function 5: cv2.erode(define which image to erode, define the kernel, define the number of iterations)

#opposite of dilation i.e erosion. The edges are going to become thinner.
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)

cv2.imshow("Greyscale image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilation image", imgDilation)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)

