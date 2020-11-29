#place all images together in a single window for better handling.
import cv2
import numpy as np

# image_path = "resources/admin.png"

# image = cv2.imread(image_path)

#using np functions and not openCV functions here.

#2 issues found here:

#--> if there are more images, it will go out of the window frame/ size will increase.
#--> the images used in the stack need to have the same number of channels. If one pic is grey and the
#other is RGB, these functions will not work since we are talking about np matrices here.

# horizontal_stack = np.hstack((image, image))

# vertical_stack = np.vstack((image, image, image))


# cv2.imshow("Horizontally stacked images", horizontal_stack)
# cv2.imshow("Vertically stacked images", vertical_stack)

#solution for the above problems - Murtaza's solution

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range (0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


image_path = "resources/admin.png"

image = cv2.imread(image_path)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageStack = stackImages(0.5, ([image, imageGray, image], [image, image, imageGray]))

cv2.imshow("Image Stack", imageStack)

cv2.waitKey(0)