import sys, os
import cv2
# import keyboard

#read an image:

#get image from folder
#script_dir = sys.path[0] #gives you the directory where the current script resides
# img_path = os.path.join(script_dir, "resources/admin.png")
#img_path = "resources/admin.png"

#read the image using the imread() method from cv2
#img = cv2.imread(img_path)

#show the image in a window called 'Ouput' using the imshow() method from cv2
#cv2.imshow("Image", img)

#the image will display and close off immediately. waitKey() method provides a delay time. 0 denotes
#an infinite delary whereas any other value apart from 0 will denote duration of milliseconds i.e 
#1000 milliseconds = 1 second
#cv2.waitKey(0)

#--------------------

#read a video object:

#video_path = "resources/massage.mp4"

#import the video
#video_capture_object = cv2.VideoCapture(video_path)

#display the video object - since a video is a sequence of images, need to loop through each frame
#one by one.
#while True:
	#success, img = video_capture_object.read() #read and store the frame in a img variable, returns True or False as a boolean too.
	#cv2.imshow("Video", img)
	#if cv2.waitKey(1) & 0xFF == ord('q'): #using '&' since it's used to compare (binary) numbers. 
	#This adds a delay of 1/1000 milliseconds and places a conditional that checks if the keypress 'q' is pressed. If so, break the loop.
		#break

#--------------------

#read a webcam object:

#import the web cam. If only one available, use 0 (to use the default webcam) 
#or if more than one webcam, type in the ID of the webcam.

webcam_capture_object = cv2.VideoCapture(0)

#set parameters before displaying it:

#define the width: id, pixels
webcam_capture_object.set(3, 640)

#define the height: id, pixels
webcam_capture_object.set(4, 480)

#change the brightness level: id, pixels
webcam_capture_object.set(10, 100)


while True:
	success, img = webcam_capture_object.read() #read and store the frame in a img variable, returns True or False as a boolean too.
	cv2.imshow("Webcam", img)
	if cv2.waitKey(1) & 0xFF == ord('q'): #using '&' since it's used to compare (binary) numbers. 
	#This adds a delay of 1/1000 milliseconds and places a conditional that checks if the keypress 'q' is pressed. If so, break the loop.
		break

#--------------------