#Face detection in an image
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#importing haarcascade model
img=cv2.imread('pic.jpeg')#we are using the image pic
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray,1.1,9)


for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    


cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
