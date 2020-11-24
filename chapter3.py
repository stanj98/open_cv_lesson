#resize and cropping an image

#By convention, in MATHEMATICS:
#1) Positive side of a x-axis is towards the east.
#2) Positive side of a y-axis is towards the NORTH.

#By convention, in OPEN-CV:
#1) Positive side of a x-axis is towards the east.
#2) But, the positive side of the y-axis is towards the SOUTH.

import cv2

#----------------------------------

#RESIZE AN IMAGE - increase/decrease the image. Increasing the image size does not determine quality.

img_path = "resources/butterfly.jpg"

image = cv2.imread(img_path)
print(image.shape) #(height, width, image channel i.e open-cv convention is BGR instead of RGB)

#resize an image using the resize() method. 
#resize(image to be resized, width, height)

image_resize = cv2.resize(image, (600, 500)) #width first, then height
print(image_resize.shape) 


#----------------------------------

#CROP AN IMAGE

#An image, in itself, is a matrix or an array of pixels.
#We can deal with images like a matrix/array.

#We dont need to use an openCV function, we can just use the matrix functionality.

#When specifying the array elements, it is a bit tricky since the resize fn. in open cv needs
#width first, then height. Here, we need to define the height first, then width.

#define the starting point and ending point for both the Height and Width

image_crop = image[1000:2000, 3000:3500] #starting : ending points of height first, then width


cv2.imshow("Image", image)

cv2.imshow("Resized Image", image_resize)

cv2.imshow("Cropped Image", image_crop)

cv2.waitKey(0)
