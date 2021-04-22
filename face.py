import cv2 as cv

face_cascade = cv.CascadeClassifier('F:/my python programs/open cv/git hub/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
img = cv.imread('F:\my python programs\open cv\images\me_4.jpg')


width = 2000
height =2000
dim = (width, height)
# resize image
resized = cv.resize(img, dim)

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(grey,1.1,3)

for(x,y,w,h) in face:
    crop=img[y:y+h,x:x+w]
img_write="result/cropped.jpg"
# cv.imwrite(img_write,crop)
cv.imshow('img',img)
cv.imshow("cropped img",crop)
cv.waitKey(0)

