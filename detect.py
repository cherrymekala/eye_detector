import cv2

cascade_classifier=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while True:
	ret,f=cap.read()
	
	gray=cv2.cvtColor(f,0)
	detect=cascade_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

	
	if(len(detect)>0):
		(x,y,w,h)=detect[0]
		f=cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
		
	cv2.imshow("sharan's mania",f)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
