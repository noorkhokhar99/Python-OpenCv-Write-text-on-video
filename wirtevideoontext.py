# Python program to write
# text on video


import cv2


cap = cv2.VideoCapture('Thanks For Watching Youtube Closing Video.mp4')

while(True):
	
	# Capture frames in the video
	ret, frame = cap.read()

	# describe the type of font
	# to be used.
	font = cv2.FONT_HERSHEY_SIMPLEX

	# Use putText() method for
	# inserting text on video
	cv2.putText(frame,
				'Thankyou for watching our channel and support us!!',
				(50, 50),
				font, 1,
				(0, 255, 255),
				2,
				cv2.LINE_4)

	# Display the resulting frame
	cv2.imshow('video', frame)

	# creating 'q' as the quit
	# button for the video
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()
